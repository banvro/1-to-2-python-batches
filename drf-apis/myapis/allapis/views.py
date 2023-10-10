from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

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