from django.urls import path
from blg import views

urlpatterns = [
    path("", views.homepage),
    path("about", views.aboutus),
    path("contact", views.contactus),
    path("services", views.services),
    path("save-data", views.savethinginfo)
]