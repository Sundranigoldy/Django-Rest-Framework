from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import viewsets

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
#now making this code more short using modelview set

# class StudentModelViewset(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers
#     #to add authenticated to login than only u can do stuff
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#testing using HTTPie i.e testing in command line only


# now using http http://127.0.0.1:8000/oneforall/ u will not be able tofetch data fetch one

# http http://127.0.0.1:8000/oneforall/ 'Authoirization:Token ur tokenno.'

#to post request
# http -f POST http://127.0.0.1:8000/oneforall/ name=jay roll=105 city=sake 'Authoirization:Token ur tokenno.'

#for put request
#http PUT http://127.0.0.1:8000/oneforall/ name=kunal roll=105 city=sakegaon 'Authoirization:Token ur tokenno.'

# for delete
#http DELETE http://127.0.0.1:8000/oneforall/id_no/ 'Authoirization:Token ur tokenno.'

#to make custom authentication

from rest_framework.permissions import IsAuthenticated
from .customauth import CustomAuthentication
class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    #to add authenticated to login than only u can do stuff
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
