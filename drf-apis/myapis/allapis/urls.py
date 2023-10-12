from django.urls import path
from allapis import views

urlpatterns = [
    path("showsomthing", views.showthis),
    path("all-conect-us-records", views.allcontact),
    path("save-conect-us-records", views.savecontactus),
    path("update-conect-us-records/<int:id>", views.updatedata),
]
