from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import viewsets


from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication

# we are adding such that anonmous user can do 2 reqyests a day while registered can do 5 request in a hour
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

#for custom throttling 
from .throttling import *
class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    #to add authenticated to login than only u can do stuff
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

#currently any user can n number of request which can maeke by server go slow hence to avoid this we use thottling concept i.e to 
#to limit the requests of our user

    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    

#now this rate is written in settings.py file..

#now suppose we have more than one class we need that everyclass should have diffn time set to do that we are
#going to make an throttling.py 
    throttle_classes = [AnonRateThrottle, ChecckRateThrottle]

    #here you can see we do 3 requests in 60 secs not more than that..
