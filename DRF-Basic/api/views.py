from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.


def student_detail(request):
# fetching data from model on basis of id

    # stu = Student.objects.get(id=2) to fetch single data

    stu = Student.objects.all() #to get all data

    # converting that complex data in python datatype for that serializer is used
    # print(stu)
    # siri = StudentSerializers(stu) for single objects to show
    siri = StudentSerializers(stu, many=True) #for all data
    # now converting that python data into json data..
    # print(siri)
    # print(siri.data)
    json_data = JSONRenderer().render(siri.data) #we can do this one line to by using jsonresponse in return
    # print(json_data)
    # sending this data to either client or on html page
    return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(siri.data, safe=True)
    #safe = false will give you list of python while safe=true will give you dict value