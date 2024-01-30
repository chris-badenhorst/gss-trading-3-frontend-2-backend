from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path("", views.addSurveys),
    path("get/", views.getSurveys),
    path("delete/<int:pk>/", views.delete_survey),
    path("register", views.register_user),
    path("login", views.login_user),
    path("get-user/<int:pk>", views.get_user),
    path("access", TokenObtainPairView.as_view()),
    path("refresh", TokenRefreshView.as_view()),
    path("verify", TokenVerifyView.as_view()),
]
