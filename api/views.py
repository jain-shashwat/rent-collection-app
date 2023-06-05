from django.shortcuts import render
from .serializers import GetBillSerializer, TenantSerializer
from rest_framework import viewsets
from .models import GetBill, Tenant

class TenantViewSet(viewsets.ModelViewSet):
 queryset = Tenant.objects.all()
 serializer_class = TenantSerializer

class GetBillViewSet(viewsets.ModelViewSet):
 queryset = GetBill.objects.all()
 serializer_class = GetBillSerializer



