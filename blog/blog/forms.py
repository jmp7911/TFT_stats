from django import forms
from django.conf import settings
from .models import Post, Comment
from django.db import models

from django_tuieditor.widgets import MarkdownEditorWidget, MarkdownViewerWidget, StaticMarkdownViewerWidget
from django_tuieditor.models import MarkdownField

class PostForm(forms.ModelForm):
  content = MarkdownField(blank=True, null=True)
  class Meta:
    model = Post
    fields = ['title', 'content', 'file_upload', 'image_upload', 'tags', 'category']
    widgets = {
      'title': forms.TextInput(
        attrs={
          'class': 'form-control',
          'placeholder': '제목을 입력하세요'
        }
      ),
      'content': MarkdownEditorWidget(),
      'image_upload': forms.ClearableFileInput(
        attrs={
          'class': 'form-control',

        }
      ),
      'file_upload': forms.ClearableFileInput(
        attrs={
          'class': 'form-control',
        }
      ),
      'tags': forms.SelectMultiple(
        attrs={
          'class': 'form-select'
        }
      ),
      'category': forms.Select(
        attrs={
          'class': 'form-select'
        }
      )
    }

class PostFormViewer(forms.ModelForm):
  content = MarkdownField(blank=True, null=True)
  class Meta:
    model = Post
    fields = ['title', 'content', 'file_upload', 'image_upload', 'tags', 'category']
    widgets = {
      'content': StaticMarkdownViewerWidget()
    }
class CommentForm(forms.ModelForm):
    class Meta:
      model = Comment

      fields = ['content']
      widgets = {
          'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40})
      }

class CommentReplyForm(forms.ModelForm):
    class Meta:
      model = Comment

      fields = ['comment_reply','content']
      widgets = {
          'comment_reply': forms.HiddenInput(),
          'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40})
      }
      