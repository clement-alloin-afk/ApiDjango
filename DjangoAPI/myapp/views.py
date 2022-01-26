from django.shortcuts import render

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