from djoser.serializers import UserCreateSerializer as BaseUserSerializer
from djoser.serializers import UserSerializer as BaseUS

class UserCreateSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id','username','email','password','first_name','last_name']

class UserSerializer(BaseUS):
    class Meta(BaseUS.Meta):
        fields = ['id','username','email','first_name','last_name']