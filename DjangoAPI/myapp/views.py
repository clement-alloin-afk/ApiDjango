from asyncio.windows_events import NULL
from cgitb import lookup
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from myapp.models import Family, User
from myapp.serializers import FamilySerializer, UserSerializer
from rest_framework import generics

class FamilyList(generics.ListCreateAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

class FamilyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def FamilyCode(request, code):
    fam = Family.objects.get(code=code)
    serializer = FamilySerializer(fam)
    return Response(serializer.data)