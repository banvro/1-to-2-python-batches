# objects -----> JSON

from rest_framework import serializers
from work.models import contactus

class cronactusyserilizer(serializers.ModelSerializer):
    class Meta: 
        model = contactus
        fields = '__all__'
        # fields = ["first_name", "phone_number"]