from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from work.serilizer import cronactusyserilizer
from work.models import contactus

# Create your views here.

@api_view(["GET", "POST"])
def fristapi(request):
    return Response({
        "message" : "my first drf api",
        "helo" : "this is helow word messgae"
    })




# JSON ---> javascript object notation

# dictionry ---> json

@api_view(["POST"])
def datasave(request):
    # print(request.data)
    data = cronactusyserilizer(data = request.data)
    if data.is_valid():
        data.save()

        return Response({
            "message" : "data saved",
            "data" : data.data
        })

    else:
        return Response({
            "message" : "Something went wrong",
            "data" : data.data
        })
    

@api_view(["GET"])
def gettingdata(request):
    data = contactus.objects.all()
    serializer = cronactusyserilizer(data, many = True)

    return Response({
        "message" : "getting data",
        "data" : serializer.data
    })

@api_view(["GET"])
def singledata(request, id):
    data = contactus.objects.filter(id = id)
    serializer = cronactusyserilizer(data, many = True)

    return Response({
        "message" : "getting data",
        "data" : serializer.data
    })

@api_view(["POST"])
def delterecord(request, id):
    data = contactus.objects.filter(id = id)
    data.delete()
    return Response({
        "message" : "data deleted sucessfully.",
    })
