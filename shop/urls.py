from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.shophome, name="shophome"),
    path("checkout/", views.checkout, name="shophome"),
    path("products/<int:myid>", views.prodview, name="shop"),
    path("contact/", views.contact, name="contact"),
    path("search/", views.search, name="Search"),
]
