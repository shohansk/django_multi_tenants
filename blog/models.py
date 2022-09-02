from django.db import models
from datetime import datetime , date
from django.contrib.auth.models import User

from tenants.models import TenantAwareModel
# Create your models here.


class Post(TenantAwareModel):
    title = models.CharField( max_length=250)
    title_tag = models.CharField( max_length=250 )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255)




