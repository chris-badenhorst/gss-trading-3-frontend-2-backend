from django.urls import path
from . import views

urlpatterns = [
    path("", views.addSurveys),
    path("get/", views.getSurveys),
]
