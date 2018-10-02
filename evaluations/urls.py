from django.conf.urls import url

from . import views

app_name='evaluations'

urlpatterns = [
    url(r"^$", views.EvaluationList.as_view(), name="all"),
    url(r"new/(?P<pk>\d+)/$", views.CreateEvaluation.as_view(), name="create"),
    url(r"by/(?P<username>[-\w]+)/$",views.UserEvaluations.as_view(),name="for_user"),
    url(r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",views.EvaluationDetail.as_view(),name="single"),
    url(r"delete/(?P<pk>\d+)/$",views.DeleteEvaluation.as_view(),name="delete"),
]
