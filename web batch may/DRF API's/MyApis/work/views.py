from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(["GET", "POST"])
def fristapi(request):
    return Response({
        "message" : "my first drf api",
        "helo" : "this is helow word messgae"
    })




# JSON ---> javascript object notation

# dictionry ---> json