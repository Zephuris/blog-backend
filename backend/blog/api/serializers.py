from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from ..models import Post,Comment,Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ['id','title']

class CategoryCreateSerializer(serializers.HyperlinkedModelSerializer):
    def save(self, **kwargs):

        category = Category.objects.create(title = self.validated_data['title'])
        return category
    class Meta:
        model = Category
        fields = ['id','title']

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Post
        fields = ['id','title','firstLetter','body','conclusion','category']
    
class PostCreateSerializer(serializers.ModelSerializer):

    def save(self, **kwargs):

        post = Post.objects.create(title = self.validated_data['title'],
                                   body = self.validated_data['body'],
                                   firstLetter = self.validated_data['firstLetter'],
                                   conclusion = self.validated_data['conclusion'],
                                   category = self.validated_data['category']
                                   )
        return post
    class Meta:
        model = Post
        fields = ['id','title','firstLetter','body','conclusion','category']
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id','name','email','content','object_id']
class CommentCreateSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):
        
        comment = Comment.objects.create(name = self.validated_data['name'],
                                        email = self.validated_data['email'],
                                        content = self.validated_data['content'],
                                        object_id = self.validated_data['object_id'],
                                        )
        
        return comment
    
    class Meta:
        model = Comment
        fields = ['id','name','email','content','object_id']


# class AuthorSerializer(serializers.ModelSerializer):

#     first_name = serializers.SerializerMethodField()
#     def get_first_name(self,Author):
#         return Author.user.first_name
#     class Meta:
#         model = Author
#         fields = ['id','first_name','nickname','postitem']

