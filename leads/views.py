from django.shortcuts import render
from rest_framework import generics
from .models import Lead
from .serializers import LeadSerializer
from rest_framework.permissions import IsAdminUser
# Create your views here.

class LeadListAPIView(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    #permission_classes = (IsAdminUser,)