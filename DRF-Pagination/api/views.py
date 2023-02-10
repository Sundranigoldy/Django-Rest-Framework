from django.shortcuts import render

# Create your views here.
from .serializers import *
from .models import *
from rest_framework.generics import ListAPIView
from .mypageno import *

class studentlist(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    # pagination_class = MyPageNumber

    # pagination_class = MyLimitoffsetPagination

    pagination_class = MyCursorPagination


#TO DECLARE GLOBALLY WE DECLARE IT IN SETTINGS.PY THATS WHERE PAGINATION IS GIVEN FOR NOW


