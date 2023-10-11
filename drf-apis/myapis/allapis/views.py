from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from allapis.models import ContactUs
from allapis.serializers import *
# Create your views here.

@api_view(["GET"])
def showthis(request):
    return Response({1 : {
        "name" : "kriss",
        "email" : "ac@gmail.com"
    }, 2 : {
        "name" : "moris",
        "email" : "moris@gmail.com"
    }})


# json

@api_view(["GET"])
def allcontact(request):
    try:
        mydata = ContactUs.objects.filter(id = 1)
        data = ContactSerlizer(mydata, many = True)
        return Response({"message" : "Contact Us fatch Sucessfully",
                        "data" : data.data})
    
    except Exception as e:
        return Response({"Error" : "Something Went Wrong"})