from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import filters
from ..models import  Post,Comment,Category
from ..permissions import isAdminOrReadOnly
from .serializers import  PostCreateSerializer, PostSerializer,CommentCreateSerializer,CommentSerializer,CategorySerializer,CategoryCreateSerializer
# Create your views here.

class PostViewSet(ModelViewSet):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = Post.objects.all()
    permission_classes = [isAdminOrReadOnly]
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostCreateSerializer
        return PostSerializer
    
    def get_serializer_context(self):
        return {'user_id':self.request.user.id}

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentCreateSerializer
        return CommentSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CategoryCreateSerializer
        return CategorySerializer
# class AuthorViewSet(ModelViewSet):
#     http_method_names = ['get']

#     queryset = Author.objects.all()

#     serializer_class = AuthorSerializer

# class CategoryViewSet(ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer