#in this we are gonna use web api to test our api not the myapp.py

from rest_framework import serializers
from .models import *

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll']
