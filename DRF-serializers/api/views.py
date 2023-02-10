from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt

#showing data in our app myapp.py
@csrf_exempt
#added becoz there is no post request
def student_api(request):
    if request.method =='GET':

        json_data=request.body
        stream = io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            siri = StudentSerializer(stu)
            json_data=JSONRenderer().render(siri.data)
            return HttpResponse(json_data, content_type='application/json')
        stu= Student.objects.all()
        siri = StudentSerializer(stu,many=True)
        json_data=JSONRenderer().render(siri.data)
        return HttpResponse(json_data, content_type='application/json')
    if request.method == "POST":
        #now which will be coming would be in json format so we need to convert to python and than to complex to store in database
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        #till now we converted data back to python format

        siri = StudentSerializer(data=pythondata)
        #here converting to complex data form
        if siri.is_valid():
            siri.save()
        #below one is reponse to myapp client wwhether data is stored or not
            res = {'msg':'Data Created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(siri.errors)
        return HttpResponse(json_data,content_type='application/json')
    #for partial update
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id = pythondata.get('id')
        stu=Student.objects.get(id=id)
        siri = StudentSerializer(stu,data=pythondata,partial=True)
        #if you are updating complete update then remove partial =true thats all
        if siri.is_valid():
             siri.save()
        #below one is reponse to myapp client wwhether data is stored or not
             res = {'msg':'Data Updated'}
             json_data=JSONRenderer().render(res)
             return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(siri.errors)
        return HttpResponse(json_data,content_type='application/json')
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg':'Data Deleted !!'}
        # json_data=JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type='application/json')
        return JsonResponse(res,safe=False)