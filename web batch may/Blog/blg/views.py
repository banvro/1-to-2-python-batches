from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, "home.html")

def aboutus(request):
    return render(request, "about.html")

def contactus(request):
    return render(request, "contact.html")

def services(request):
    return render(request, "Services.html")