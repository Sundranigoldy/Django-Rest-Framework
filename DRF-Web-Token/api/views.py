from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import viewsets


from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    #to add authenticated to login than only u can do stuff
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

#http POST http://127.0.0.1:8000/gettoken/ username="user1" password="Goldy123@"  
# above to generate token
# 
#http http://127.0.0.1:8000/oneforall/ 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc1OTI5NzM0LCJpYXQiOjE2NzU5Mjk0MzQsImp0aSI6IjVjM2U2MDhhMTllNjRmZTQ5ZGVhNTAwY2QzN2Q5YzljIiwidXNlcl9pZCI6Mn0.6zPN-12ef6mfPG7Vy3SZMbRahjoB50FX9YYHG0x6jVE
# than to get access using token we use above
# 
# to post data
# http -f POST http://127.0.0.1:8000/oneforall/oneforall/ name=raj city=bl, roll=141 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc1OTI5NzM0LCJpYXQiOjE2NzU5Mjk0MzQsImp0aSI6IjVjM2U2MDhhMTllNjRmZTQ5ZGVhNTAwY2QzN2Q5YzljIiwidXNlcl9pZCI6Mn0.6zPN-12ef6mfPG7Vy3SZMbRahjoB50FX9YYHG0x6jVE                         

#if user has permission he would be able to add
# to update
#http PUT http://127.0.0.1:8000/oneforall/oneforall/3/ name=kunal city=bl, roll=111 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc1OTI5NzM0LCJpYXQiOjE2NzU5Mjk0MzQsImp0aSI6IjVjM2U2MDhhMTllNjRmZTQ5ZGVhNTAwY2QzN2Q5YzljIiwidXNlcl9pZCI6Mn0.6zPN-12ef6mfPG7Vy3SZMbRahjoB50FX9YYHG0x6jVE                         

#to delete
#http DELETE http://127.0.0.1:8000/oneforall/oneforall/3/ 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc1OTI5NzM0LCJpYXQiOjE2NzU5Mjk0MzQsImp0aSI6IjVjM2U2MDhhMTllNjRmZTQ5ZGVhNTAwY2QzN2Q5YzljIiwidXNlcl9pZCI6Mn0.6zPN-12ef6mfPG7Vy3SZMbRahjoB50FX9YYHG0x6jVE                         
