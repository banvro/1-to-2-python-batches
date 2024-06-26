from django.urls import path
from work import views

urlpatterns = [
    path("first-api", views.fristapi),
    path("saving-data", views.datasave),
    path("getting-data", views.gettingdata),
    path("single-record/<int:id>", views.singledata),
    path("delete-record/<int:id>", views.delterecord),
] 