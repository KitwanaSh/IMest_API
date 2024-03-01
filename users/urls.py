from django.urls import path
from . import views

urlpatterns = [
    path("singup/", views.signup),
    path("login/", views.user_login)
]
