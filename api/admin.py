from django.contrib import admin
from .models import GetBill, Tenant

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
 list_display = ['id', 'tenant_name', 'members', 'rent_paid', 'wallet', 'dispute', 'docsverified']

@admin.register(GetBill)
class GetBillAdmin(admin.ModelAdmin):
 list_display = ['id', 'electricity', 'water', 'maintainence']

