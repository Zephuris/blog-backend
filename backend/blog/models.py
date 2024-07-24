from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.title
    
class Post(models.Model):
    title = models.CharField(max_length=20)
    firstLetter = models.TextField()
    body = models.TextField()
    conclusion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

class Comment(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    object_id = models.PositiveIntegerField()

