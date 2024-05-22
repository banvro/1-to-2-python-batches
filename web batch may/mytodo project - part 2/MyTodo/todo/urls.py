from django.urls import path
from todo import views

urlpatterns = [
    path("", views.homepage, name = "home"),
    path("savedata", views.savingtodo),
    path("delte-todo/<int:myid>", views.deltetodo),
    path("update-todo/<int:todoid>", views.updatingttodo),
    path("update-this-todo/<int:todoid>", views.updatingthisttodo),
]