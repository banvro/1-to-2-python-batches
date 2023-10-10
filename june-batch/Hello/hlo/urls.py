from django.urls import path, include
from hlo import views
urlpatterns = [
    path("", views.home, name = "home"),
    path("update/<int:id>", views.update, name = "update"),
    path("updatethis/<int:id>", views.updatethis, name = "updatethis"),
    path("showdata", views.showdata, name = "showdata"),
    path("delect/<int:id>", views.deletme)
]