from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
   def get(self, request, *args, **kwargs):
      queryset = Post.objects.all()
      serializer_class = PostSerializer