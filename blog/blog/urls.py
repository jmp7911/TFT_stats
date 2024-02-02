from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostAPIView

router = DefaultRouter()
router.register('', PostAPIView)
urlpatterns = [
    path('', include(router.urls)),
]

