from django.shortcuts import render
from rest_framework import generics
from .models import Opportunity
from .serializers import OpportunitySerializer
from rest_framework.permissions import IsAdminUser
# Create your views here.

class OpportunityListAPIView(generics.ListCreateAPIView):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer
    #permission_classes = (IsAdminUser,)
