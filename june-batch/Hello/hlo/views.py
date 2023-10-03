from django.shortcuts import render
from hlo.models import ContactUs
# Create your views here.

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("number")
        email = request.POST.get("emial")
        msg = request.POST.get("msg")

        savedata = ContactUs(Name = name, Number = number, Emial = email, Message = msg)
        savedata.save()
    return render(request, "home.html")