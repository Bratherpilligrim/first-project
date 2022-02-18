from rest_framework import serializers
from .models import *


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Home
        fields = '__all__'
    
    
    
    

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'