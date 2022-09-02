from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from blog.serializers import PostSerializer
from rest_framework.response import Response
from blog.models import Post



from rest_framework import permissions


from rest_framework import status, viewsets

from rest_framework import generics
from tenants.Utilites import get_tenant 


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer