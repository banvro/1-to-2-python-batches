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
    
@api_view(["POST"])
def savecontactus(request):
    print(request.data)
    savemydata = ContactSerlizer(data = request.data)
    if savemydata.is_valid():
        savemydata.save()
    return Response({"data" : "Data saved sucessfully..",
                     "Data" : savemydata.data})

@api_view(["PATCH"])
def updatedata(request, id):
    obj = ContactUs.objects.get(id = id)
    seri = ContactSerlizer(obj, data = request.data, partial = True)
    if seri.is_valid():
        seri.save()
    return Response({"data" : "Data Update sucessfully..",
                     "user id" : id,
                     "mydata" : seri.data})
