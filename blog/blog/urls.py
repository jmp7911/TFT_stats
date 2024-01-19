from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='blog'),
    path('view/<int:pk>/', views.view, name='view'),
    path('write/', views.write, name='write'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('deleteMultiple/', views.BoardDeleteMultiple.as_view(), name='deleteMultiple'),
    # url(r'^search/$', views.search, name='search'),
]
