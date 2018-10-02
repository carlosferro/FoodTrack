from django.conf.urls import url

from . import views

app_name = 'trucks'

urlpatterns = [
    url(r"^$", views.ListTrucks.as_view(), name="all"),
    url(r"^new/$", views.CreateTruck.as_view(), name="create"),
    url(r"^evaluations/in/(?P<slug>[-\w]+)/$",views.SingleTruck.as_view(),name="single"),
    url(r"join/(?P<slug>[-\w]+)/$",views.FollowTruck.as_view(),name="follow"),
    url(r"leave/(?P<slug>[-\w]+)/$",views.UnfollowTruck.as_view(),name="unfollow"),
    url(r"delete/(?P<pk>\d+)/$",views.DeleteTruck.as_view(),name="delete"),
]
