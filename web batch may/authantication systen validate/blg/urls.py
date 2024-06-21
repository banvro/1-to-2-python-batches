from django.urls import path
from blg import views

urlpatterns = [
    path("", views.homepage),
    path("about", views.aboutus),
    path("contact", views.contactus),
    path("services", views.services, name="services"),
    path("save-data", views.savethinginfo),
    path("delete-this/<int:xyz>", views.deletethis),
    path("updatedata/<int:abc>", views.updatedata),
    path("updatedata-now/<int:ab>", views.updatrdaa),

    path("signup", views.signuppage),
    path("login", views.loginn),
    path("logout-user", views.logoutnow),
]