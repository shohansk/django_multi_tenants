from django.shortcuts import render

# Create your views here.
from .models import Member
from .Utilites import get_tenant


def our_team(request):
    tenant = get_tenant(request)
    members = Member.objects.filter(tenant=tenant)


    return render(request, 'tenants/our_team.html',{'tenants': tenant, 'members':members})
