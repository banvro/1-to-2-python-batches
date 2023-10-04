from django.urls import path, include
from hlo import views
urlpatterns = [
    path("", views.home, name = "home"),
    path("showdata", views.showdata, name = "showdata"),
    path("delect/<int:id>", views.deletme)
]