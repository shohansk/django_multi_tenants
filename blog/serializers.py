from dataclasses import fields
from django.contrib.auth.models import User, Group
from rest_framework import serializers

from blog.models import Post





class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields ='__all__'