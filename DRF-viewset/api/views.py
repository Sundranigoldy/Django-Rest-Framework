from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import viewsets

#for authentication

from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from .custompermissions import *

# for function based view we need following import

# from rest_framework.decorators import api_view, authentication_classes,permission_classes
# from rest_framework.authentication import BasicAuthentication, SessionAuthentication
# from rest_framework.permissions import IsAuthenticated

# class StudentViewset(viewsets.ViewSet):
#     def list(self, request):
#         stu = Student.objects.all()
#         siri = StudentSerializers(stu, many=True)
#         return Response(siri.data)
    
#     def retrive(self,request,pk=None):
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             siri = StudentSerializers(stu)
#             return Response(siri.data)
#     def create(self,request):
#         siri = StudentSerializers(data = request.data)
#         if siri.is_valid():
#             siri.save()
#             return Response({'msg':'Data Created'})
#         return Response(siri.errors)
#     def update(self,request,pk):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         siri = StudentSerializers(stu,data=request.data)
#         if siri.is_valid():
#             siri.save()
#             return Response({'msg':'Complete Data Updated'})
#         return Response(siri.errors)
#     def partial_update(self,request,pk):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         siri = StudentSerializers(stu,data=request.data,partial=True)
#         if siri.is_valid():
#             siri.save()
#             return Response({'msg':'Partial Data Updated'})
#         return Response(siri.errors)
#     def destroy(self,request,pk):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'DATA DELETED'})



#read only model view set

# class StudentROModelViewset(viewsets.ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers
    

#now making this code more short using modelview set

class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    #to add authenticated to login than only u can do stuff
    authentication_classes = [SessionAuthentication]
    
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [IsAdminUser]
    
    
    # permission_classes = [DjangoModelPermissions]
    

    #by using above u can give custom permissions to user as per needed 
    
    
    
    # but it also doesnt allow any unregistered user to read
    # for that we use below
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

#using customs permissions which we have created using custom permissionss

    # permission_classes =[MyPermission]


#this is just for single class but if u need to define it gloablly for many classes than 
#you need to below code in settings

'''
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':['rest_framework.authentication.BasicAuthentication'],
    'DEFAULT_PERMISSION_CLASSES':['rest_framework.permissions.IsAuthenticated']
}
'''




#now we can also give these types of permission to function based view..

# @api_view(['GET','POST','PUT','PATCH','DELETE'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
# # if nothing is return in api view it is get function automatically
# def web_api_test(request,pk=None):
#     if request.method == 'GET':
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             siri = StudentSerializers(stu)
#             return Response(siri.data)
#         stu = Student.objects.all()
#         siri = StudentSerializers(stu,many=True)
#         return Response(siri.data)
#     if request.method == 'POST':
#         siri = StudentSerializers(data = request.data)
#         if siri.is_valid():
#             siri.save()
#             return Response({'msg':'Data Created'})
#         return Response(siri.errors)
#     if request.method == 'PUT':
#         id = pk
#         stu = Student.objects.get(pk=id)
#         siri = StudentSerializers(stu,data=request.data)
#         if siri.is_valid():
#             siri.save()
#             return Response({'msg':'Complete Data Updated'})
#         return Response(siri.errors)
#     if request.method == 'PATCH':
#         id = pk
#         stu = Student.objects.get(pk=id)
#         siri = StudentSerializers(stu,data=request.data,partial=True)
#         if siri.is_valid():
#             siri.save()
#             return Response({'msg':'Partial Data Updated'})
#         return Response(siri.errors)
#     if request.method == 'DELETE':
#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'DATA DELETED'})


