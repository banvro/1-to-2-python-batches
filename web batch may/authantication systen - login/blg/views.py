from django.shortcuts import render, redirect
from django.http import HttpResponse
from blg.models import ContactUs
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


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
        image = request.FILES.get("img")
        # print(name, email, phone_num, mesag)
        print("my image :", image)

        # data = ContactUs(Full_Name = name, Email = email, Phone_number = phone_num, Message = mesag, saveimg = image)
        # data.save()

        msg = EmailMessage("This si django Test", "this is email body", "banvro7@gmail.com", ["banvro07@gmail.com"])
        msg.send()

        return redirect("/about")

    return HttpResponse("Data Saved")



def deletethis(request, xyz):
    data = ContactUs.objects.get(id = xyz)
    
    data.delete()

    return redirect("/about")


def updatedata(request, abc):
    data = ContactUs.objects.get(id = abc)
    return render(request, "contactusupdae.html", {"data" : data})


def updatrdaa(request, ab):
    data = ContactUs.objects.get(id = ab)
    if request.method == "POST":
        name = request.POST.get("fname")
        email = request.POST.get("myemail")
        phone_num = request.POST.get("pnumber")
        mesag = request.POST.get("msg")

        data.Full_Name = name 
        data.Email = email
        data.Phone_number = phone_num
        data.Message = mesag
        data.save()
    
        return redirect("/about")


def signuppage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        full_name = request.POST.get("fname")
        password = request.POST.get("pass")

        new_user = User.objects.create_user(username = username, email = email, first_name = full_name, password = password)
        new_user.save()

    return render(request, "auth/signup.html")

def loginn(request):
    if request.method == "POST":
        usernmae = request.POST.get("u")
        password = request.POST.get("p")

        user = authenticate(username = usernmae, password = password)

        if user is not None:
            login(request, user)

            return redirect("services")
        

    return render(request, "auth/login.html")


def logoutnow(request):
    logout(request)
    return redirect("services")