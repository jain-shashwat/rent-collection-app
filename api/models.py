from django.db import models

class Tenant(models.Model):
    tenant_name = models.CharField(max_length = 100)
    members = models.IntegerField()
    rent_paid = models.BooleanField(default = False)
    wallet = models.DecimalField(max_digits = 100000, decimal_places=2, default=0)
    dispute = models.BooleanField(default = False)
    docsverified = models.BooleanField(default = False)

    def __str__(self):
        return self.tenant_name

class GetBill(models.Model):
    electricity = models.CharField(max_length=20, default='pending')
    water = models.CharField(max_length=20, default='pending')
    maintainence = models.CharField(max_length=20, default='pending')
    tenant = models.ForeignKey(Tenant, on_delete = models.CASCADE, related_name = 'bill')

    def __str__(self):
        return (self.electricity +' '+ self.water +' '+ self.maintainence)

