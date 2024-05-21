from django.urls import path
from todo import views

urlpatterns = [
    path("", views.homepage, name = "home"),
    path("savedata", views.savingtodo)
]