from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   path("", views.home, name="home"),
   path("plan/", views.plan, name="plan"),
   path("contact/", views.contact, name="contact"),
   path("bmr/", views.bmr, name="bmr"),
   path("blog/", views.blog, name="blog"),
   path("Register/", views.Register, name="Register"),
]
