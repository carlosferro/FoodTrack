from django import forms

from evaluations import models


class EvaluationForm(forms.ModelForm):
    class Meta:
        model = models.Evaluation
        fields = ["message","rating"]
        widgets = {
            'rating':forms.RadioSelect(),
        }

    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop("user", None)
    #     super().__init__(*args, **kwargs)
    #     if user is not None:
    #         self.fields["truck"].queryset = (
    #             models.Truck.objects.filter(
    #                 pk__in=user.trucks.values_list("truck__pk")
    #             )
    #         )
