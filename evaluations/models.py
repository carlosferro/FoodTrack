from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

import misaka

from trucks.models import  Truck

from django.contrib.auth import get_user_model
User = get_user_model()


class Evaluation(models.Model):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    STARS_CHOICES = ((ZERO, '0'),
                        (ONE, '1'),
                        (TWO, '2'),
                        (THREE, '3'),
                        (FOUR, '4'),
                        (FIVE, '5'),)

    user = models.ForeignKey(User, related_name="evaluations")
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    truck = models.ForeignKey(Truck, related_name="evaluations",null=True, blank=True)
    rating = models.DecimalField(choices=STARS_CHOICES, default=1, max_digits=2, decimal_places=1)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "evaluations:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user", "message"]
