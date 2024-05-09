from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
 
def homepage(request):
    # return HttpResponse("this is a home page...")
    return render(request, "home.html")


def myblog(request):
    return render(request, "blog1.html")
    # return HttpResponse("this is a blog page")

def loginpage(request):
    return render(request, "auth/login.html")