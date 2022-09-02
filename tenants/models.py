from django.db import models

# Create your models here.
class Tenants(models.Model):
    name = models.CharField(max_length=255)
    subdomain = models.CharField(max_length=255)

class TenantAwareModel(models.Model):
    tenant = models.ForeignKey(Tenants,on_delete=models.CASCADE)

class Member(TenantAwareModel):
    name = models.CharField(max_length=255)
