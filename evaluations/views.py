from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin

from . import forms
from . import models

from django.contrib.auth import get_user_model
User = get_user_model()


class EvaluationList(SelectRelatedMixin, generic.ListView):
    model = models.Evaluation
    select_related = ("user", "truck")


class UserEvaluations(generic.ListView):
    model = models.Evaluation
    template_name = "evaluations/user_evaluation_list.html"

    def get_queryset(self):
        try:
            self.evaluation_user = User.objects.prefetch_related("evaluations").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.evaluation_user.evaluations.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["evaluation_user"] = self.evaluation_user
        return context


class EvaluationDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Evaluation
    select_related = ("user", "truck")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )


class CreateEvaluation(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    form_class = forms.EvaluationForm
    model = models.Evaluation

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({"user": self.request.user})
    #     return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.truck = models.Truck.objects.get(pk=self.kwargs['pk'])
        self.object.save()
        return super().form_valid(form)


class DeleteEvaluation(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Evaluation
    select_related = ("user", "truck")
    success_url = reverse_lazy("evaluations:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Evaluation Deleted")
        return super().delete(*args, **kwargs)
