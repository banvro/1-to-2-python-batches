from django.shortcuts import render, redirect
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
    return render(request, "home.html", {"show" : "home"})

def update(request, id):
    data = ContactUs.objects.get(id = id)
    return render(request, "home.html", {"show" : "update", "mydata" : data})


def updatethis(request, id):
    data = ContactUs.objects.get(id = id)
    if request.method == "POST":
        print("iiiiiiiiiiiii")
        name = request.POST.get("name")
        number = request.POST.get("number")
        email = request.POST.get("emial")
        msg = request.POST.get("msg")

        data.Name = name
        data.Number = number 
        data.Emial = email
        data.Message = msg 
        data.save()
    return redirect("/")



def showdata(request):
    data = ContactUs.objects.all()
    return render(request, "showdata.html", {"mydata" : data})


def deletme(request, id):
    data = ContactUs.objects.get(id = id)
    data.delete()
    return redirect("showdata")

