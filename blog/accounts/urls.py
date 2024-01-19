from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/<int:pk>/update/', views.profile, name='profile'),
    path('profile/<int:pk>/password/', views.password_change, name='password_change'),
    path('profile/password_change_done/', views.password_change_done, name='password_change_done'),
    
]