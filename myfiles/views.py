from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.generics import ListAPIView
# Create your views here.
from rest_framework.permissions import IsAuthenticated

from myfiles.serilazers import Api_Serializer
from myfiles.models import Teacher


class ListApi(ListAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    queryset = Teacher.objects.all()
    serializer_class = Api_Serializer
    permission_classes = (IsAuthenticated,)
