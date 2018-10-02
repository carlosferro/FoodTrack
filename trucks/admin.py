from django.contrib import admin

from . import models


class TruckFollowerInline(admin.TabularInline):
    model = models.TruckFollower



admin.site.register(models.Truck)
