from django.shortcuts import render, redirect
from django.http import HttpResponse
from blg.models import ContactUs

# Create your views here.

def homepage(request):
    return render(request, "home.html")

def aboutus(request):
    data = ContactUs.objects.all().order_by("-id")
    # print(data)
    return render(request, "about.html", {"mydata" : data})

def contactus(request):
    return render(request, "contact.html")

def services(request):
    return render(request, "Services.html")



def savethinginfo(request):
    if request.method == "POST":
        name = request.POST.get("fname")
        email = request.POST.get("myemail")
        phone_num = request.POST.get("pnumber")
        mesag = request.POST.get("msg")
        print(name, email, phone_num, mesag)

        data = ContactUs(Full_Name = name, Email = email, Phone_number = phone_num, Message = mesag)
        data.save()

        return redirect("/about")

    return HttpResponse("Data Saved")



def deletethis(request, xyz):
    data = ContactUs.objects.get(id = xyz)
    
    data.delete()

    return redirect("/about")