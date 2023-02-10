# from django.shortcuts import render

# # Create your views here.
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import *
# from .serializers import *

# #for class based api we need below import
# from rest_framework.views import APIView



# #function based view

# # @api_view(['GET','POST','PUT','PATCH','DELETE'])
# #if nothing is return in api view it is get function automatically
# # def web_api_test(request,pk=None):
# #     if request.method == 'GET':
# #         id = pk
# #         if id is not None:
# #             stu = Student.objects.get(id=id)
# #             siri = StudentSerializers(stu)
# #             return Response(siri.data)
# #         stu = Student.objects.all()
# #         siri = StudentSerializers(stu,many=True)
# #         return Response(siri.data)
# #     if request.method == 'POST':
# #         siri = StudentSerializers(data = request.data)
# #         if siri.is_valid():
# #             siri.save()
# #             return Response({'msg':'Data Created'})
# #         return Response(siri.errors)
# #     if request.method == 'PUT':
# #         id = pk
# #         stu = Student.objects.get(pk=id)
# #         siri = StudentSerializers(stu,data=request.data)
# #         if siri.is_valid():
# #             siri.save()
# #             return Response({'msg':'Complete Data Updated'})
# #         return Response(siri.errors)
# #     if request.method == 'PATCH':
# #         id = pk
# #         stu = Student.objects.get(pk=id)
# #         siri = StudentSerializers(stu,data=request.data,partial=True)
# #         if siri.is_valid():
# #             siri.save()
# #             return Response({'msg':'Partial Data Updated'})
# #         return Response(siri.errors)
# #     if request.method == 'DELETE':
# #         id = pk
# #         stu = Student.objects.get(pk=id)
# #         stu.delete()
# #         return Response({'msg':'DATA DELETED'})



# #class based view


# class StudentAPI(APIView):
#     def get(self,request,pk=None,format=None):
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             siri = StudentSerializers(stu)
#             return Response(siri.data)
#         stu = Student.objects.all()
#         siri = StudentSerializers(stu,many=True)
#         return Response(siri.data)
#     def post(self,request,format=None):
#         siri = StudentSerializers(data = request.data)
#         if siri.is_valid():
#             siri.save()
#             return Response({'msg':'Data Created'})
#         return Response(siri.errors)
#     def put(self,pk,request,format=None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         siri = StudentSerializers(stu,data=request.data)
#         if siri.is_valid():
#             siri.save()
#             return Response({'msg':'Complete Data Updated'})
#         return Response(siri.errors)
#     def patch(self,request,pk,format=None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         siri = StudentSerializers(stu,data=request.data,partial=True)
#         if siri.is_valid():
#             siri.save()
#             return Response({'msg':'Partial Data Updated'})
#         return Response(siri.errors)
    
#     def delete(self,request,pk,format=None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'DATA DELETED'})


#now here we are gonna use Generic APIview to do these stuff

#Generic APiView and model mixin

from .models import *
from .serializers import *
from rest_framework.generics import  GenericAPIView, ListAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin


# class StudentList(GenericAPIView,ListModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers


#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

# class StudentCreate(GenericAPIView,CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers


#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

# class StudentRetrive(GenericAPIView,RetrieveModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers


#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)

# class StudentUpdate(GenericAPIView,UpdateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers


#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)

# class StudentDestroy(GenericAPIView,DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers


#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)


#now we will see how can we do in single class to do all like in function based we doo..

#now we do grpuping  where pk is not required


# class LCStudent(GenericAPIView,ListModelMixin, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers


#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
    
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)


# class RUDStudent(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers


#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
    
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)

#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)




#concrete view classesss
#here you dont need to that much lines just in 2 lines it will be done

class LCStudent(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

# class RUStudent(RetrieveUpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers

# class RdStudent(RetrieveDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers
class RudStudent(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers