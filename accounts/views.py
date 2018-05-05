from django.shortcuts import render
from rest_framework import generics
from .models import Account
from .serializers import AccountSerializer
from rest_framework.permissions import IsAdminUser
# Create your views here.

class AccountListAPIView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    #permission_classes = (IsAdminUser,)