from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from django.core.urlresolvers import reverse, reverse_lazy
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from trucks.models import Truck,TruckFollower
from . import models

class CreateTruck(LoginRequiredMixin, generic.CreateView):
    fields = ("name", "description")
    model = Truck

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class SingleTruck(generic.DetailView):
    model = Truck

class ListTrucks(generic.ListView):
    model = Truck

class DeleteTruck(LoginRequiredMixin, generic.DeleteView):
    model = models.Truck
    # select_related = ("user", "truck")
    success_url = reverse_lazy("trucks:all")

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Truck Deleted")
        return super().delete(*args, **kwargs)


class FollowTruck(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("trucks:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        truck = get_object_or_404(Truck,slug=self.kwargs.get("slug"))

        try:
            TruckFollower.objects.create(user=self.request.user,truck=truck)

        except IntegrityError:
            messages.warning(self.request,("Warning, already following {}".format(truck.name)))

        else:
            messages.success(self.request,"You are now following {} truck.".format(truck.name))

        return super().get(request, *args, **kwargs)


class UnfollowTruck(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("trucks:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):

        try:

            membership = models.TruckFollower.objects.filter(
                user=self.request.user,
                truck__slug=self.kwargs.get("slug")
            ).get()

        except models.TruckFollower.DoesNotExist:
            messages.warning(
                self.request,
                "You can't unfollow this truck because you aren't following it."
            )
        else:
            membership.delete()
            messages.success(
                self.request,
                "You have successfully unfollow this truck."
            )
        return super().get(request, *args, **kwargs)
