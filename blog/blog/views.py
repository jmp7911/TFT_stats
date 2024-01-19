from django import template
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormMixin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify
from .forms import PostForm, CommentForm, CommentReplyForm, PostFormViewer
from django.urls import reverse_lazy

from .models import Post, Category, Tag, Comment
from django.conf import settings
import markdown
from django.utils.safestring import mark_safe
from markdown.extensions.toc import TocExtension
from django.db.models import Q, Count
from django.views.decorators.csrf import csrf_exempt

class PageTitleViewMixin:
  title = ""

  def get_title(self):
    return self.title
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = self.get_title()
    return context
 
class BoardList(PageTitleViewMixin, ListView):
  title = '게시글 목록'
  model = Post
  paginate_by = 6
  context_object_name = 'post_list'
  
  def get_context_data(self, **kwargs):
    # request의 GET 파라미터에서 'q'를 가져옵니다.
    search = self.request.GET.get('search', '')
    sel_category = self.request.GET.get('category', '')
    sort = self.request.GET.get('sort', '')
    context = super().get_context_data(**kwargs)
    count = len(self.object_list)
    category = Category.objects.all()

    if search:
      context['search'] = search
    if sel_category:
      category = category.extra(select={'is_sel_category':'id = '+sel_category})
    
    context['count'] = count
    context['category'] = category
    context['sort'] = sort

    return context
  
  def get_queryset(self):
    queryset = super().get_queryset().annotate(number_of_comments=Count('comment'))

    # request의 GET 파라미터에서 'q'를 가져옵니다.
    search = self.request.GET.get('search', '')
    cate = self.request.GET.get('category', '')
    
    q = Q()
    # 'q' 파라미터가 제공되었을 경우, 쿼리셋을 필터링합니다.
    if search:
      q &= (Q(title__icontains=search) | Q(content__icontains=search))
    if cate:
      q &= Q(category=cate)

    return queryset.filter(q)
  
  def get_ordering(self):
    sort = self.request.GET.get('sort', 'created_at')
    ordering = ['-'+sort]
    return ordering

class BoardWrite(PageTitleViewMixin, PermissionRequiredMixin, CreateView):
  form_class = PostForm
  permission_required = 'blog.add_post'
  title = '게시글 작성'
  model = Post
  context_object_name = 'post'
  def form_valid(self, form):
    post = form.save(commit=False)
    post.user = self.request.user
    post.save()
    return super().form_valid(form)
  
 
class BoardUpdate(PageTitleViewMixin, PermissionRequiredMixin, UpdateView):
  permission_required = 'blog.change_post'
  form_class = PostForm
  title = '게시글 수정'
  model = Post
  context_object_name = 'post'
  
class BoardView(PageTitleViewMixin, DetailView):
  title = '게시글 보기'
  model = Post
  context_object_name = 'post'
  form_class = PostFormViewer
  
  def get_context_data(self, **kwargs):
    context = super(BoardView, self).get_context_data(**kwargs)
    if self.request.GET.get('comment'):
      comment = Comment.objects.get(id=self.request.GET.get('comment'))
      context['comment_reply_form'] = CommentReplyForm()
      context['comment_reply_form'].fields['comment_reply'].initial = comment.id
      context['comment_id'] = comment.id
    
      
    context['comment_form'] = CommentForm()
    post = super(BoardView, self).get_object(queryset=None)
    context['form'] = PostFormViewer(initial={'content':post.content})
    comments = Comment.objects.filter(post=post.id)
    context['comments'] = comments
    return context
  def get(self, request, *args, **kwargs):
    response = super(BoardView, self).get(request, *args, **kwargs)
    if request.GET.get('comment') and not request.user.is_authenticated:
      return redirect('login')
    #조회수 반영
    self.object.increase_views()

    return response
  
  def post(self, request, *args, **kwargs):
    post = super(BoardView, self).get_object(queryset=None)
    if self.request.POST.get('comment_reply'):
      comment_form = CommentReplyForm(request.POST)
    else:
      comment_form = CommentForm(request.POST)
      
    
    if comment_form.is_valid():
      comment = comment_form.save(commit=False)
      comment.post = post
      comment.user = request.user
      
      comment.save()
      
      return redirect(post.get_absolute_url())
    else:
      return redirect('blog')

  def get_object(self, queryset=None):
    post = super(BoardView, self).get_object(queryset=None)
    if post.file_upload:
      post.file_upload = str(post.file_upload).split('/')[-1]
    return post
  
class BoardDelete(PageTitleViewMixin, PermissionRequiredMixin, DeleteView):
  permission_required = "blog.delete_post"
  title = '게시글 삭제'
  model = Post
  context_object_name = 'post'
  success_url = reverse_lazy('blog')
  
  def get(self, *args, **kwargs):
    return self.post(*args, **kwargs)
    
class BoardDeleteMultiple(View):
  title = '게시글 선택 삭제'
  
  def post(self, *args, **kwargs):
    print(f'request: {self.request.POST}')
    
    if self.request.user.is_staff:
      data = self.request.POST.getlist('data[]')

      Post.objects.filter(id__in=data).delete()
    return redirect('blog')


index = BoardList.as_view()
write = login_required(BoardWrite.as_view())
update = BoardUpdate.as_view()
view = BoardView.as_view()
delete = BoardDelete.as_view()