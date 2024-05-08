from django.urls import path
from blog import views

urlpatterns = [
    # path(url, fuction from view, unique name)
    path("home", views.homepage, name = "home"),
    path("blog1", views.myblog)
]