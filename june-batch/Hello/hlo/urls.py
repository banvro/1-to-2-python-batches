from django.urls import path, include
from hlo import views
urlpatterns = [
    path("", views.home)
]