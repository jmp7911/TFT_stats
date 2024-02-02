from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import Post, Tag

class UsernameSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = ['email']
class PostSerializer(ModelSerializer):
  class Meta:
    model = Post
    fields = '__all__'

class PostUserSerializer(ModelSerializer):
  user = UsernameSerializer()
  class Meta:
    model = Post
    fields = '__all__'
