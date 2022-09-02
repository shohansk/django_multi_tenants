from django.contrib import admin

# Register your models here.
from .models import Member,Tenants

admin.site.register(Tenants)
admin.site.register(Member)