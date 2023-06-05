from .models import GetBill, Tenant
from rest_framework import serializers

class GetBillSerializer(serializers.ModelSerializer):
 class Meta:
  model = GetBill
  fields = "__all__"

class TenantSerializer(serializers.ModelSerializer):
 bill = GetBillSerializer(many=True, read_only=True)
 class Meta:
  model = Tenant
  fields = ['id', 'tenant_name', 'members', 'bill', 'rent_paid', 'wallet', 'dispute', 'docsverified']


# ['id', 'tenant_name', 'members', 'bill', 'rent_paid', 'wallet', 'dispute', 'docsverified']