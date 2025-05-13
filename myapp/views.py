from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from myapp.models import Remind
from rest_framework.response import Response
from myapp.serializers import RemindSerializer
class RemindListCreateApiView(ListCreateAPIView):
    queryset=Remind.objects.all()
    serializer_class=RemindSerializer
class RemindRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset=Remind.objects.all()
    serializer_class=RemindSerializer
    lookup_field='id'
