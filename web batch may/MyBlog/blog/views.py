from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
 
def homepage(request):
    return HttpResponse("this is a home page...")


def myblog(request):
    return HttpResponse("this is a blog page")