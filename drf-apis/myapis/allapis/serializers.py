from rest_framework import serializers
from allapis.models import *


class ContactSerlizer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__' 
