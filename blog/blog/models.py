import logging
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from abc import abstractmethod
from django.utils.translation import gettext_lazy as _

User = get_user_model()
logger = logging.getLogger(__name__)

class BaseModel(models.Model):
    def save(self, *args, **kwargs):
        is_update_views = isinstance(
            self,
            Post) and 'update_fields' in kwargs and kwargs['update_fields'] == ['hits']
        if is_update_views:
            Post.objects.filter(pk=self.pk).update(hits=self.hits)
        else:
            super().save(*args, **kwargs)
    
    class Meta:
        abstract = True

    @abstractmethod
    def get_absolute_url(self):
        pass
      
class Category(models.Model):
  name = models.CharField(max_length=100, unique=True)
  
  def __str__(self):
    return self.name
  
class Tag(models.Model):
  name = models.CharField(max_length=100, unique=True)
  
  def __str__(self):
    return self.name

class Post(BaseModel):
  title = models.CharField(max_length=100)
  content = models.TextField()
  image_upload = models.ImageField(verbose_name='이미지',upload_to='blog/%Y/%m/%d/', blank=True, null=True)
  file_upload = models.FileField(verbose_name='파일',upload_to='file/%Y/%m/%d/', blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
  hits = models.IntegerField(default=0)
  category = models.ForeignKey(Category, blank=True, null=True ,on_delete=models.CASCADE)
  tags = models.ManyToManyField(Tag, blank=True)
  
  def __str__(self):
    return self.title
    
  def increase_views(self):
    self.hits += 1
    self.save(update_fields=['hits'])
  
  def get_absolute_url(self):
    return reverse('view', kwargs={'pk':self.pk})
  
    
class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  comment_reply = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
  comment_order = models.IntegerField(null=True, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  
  def __str__(self):
    return self.content
  
      
