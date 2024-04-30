from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from django.contrib.auth.decorators import login_required
from .views import MyPasswordChangeView, MyPasswordSetView
from django.conf import settings

from conf.views import (
    
    dashboard_view,
    dashboard_analytics_view,
    dashboard_crypto_view,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('dj_rest_auth.urls')),
    path('api/accounts/registration/', include('dj_rest_auth.registration.urls')),
    path('blog/', include('blog.urls')),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    
    # dashboard
    path('',view=dashboard_view,name='dashboard'),
    path('dashboard_analytics',view=dashboard_analytics_view,name='dashboard_analytics'),
    path('dashboard_crypto',view=dashboard_crypto_view,name='dashboard_crypto'),
    

    # apps
    path('apps/',include('apps.urls')),
    
    # pages
    path('pages/',include('pages.urls')),
    
    # components
    path('components/',include('components.urls')),
    
    # summoners
    path('summoners/',include('summoners.urls')),
    
    path(
        "account/password/change/",
        login_required(MyPasswordChangeView.as_view()),
        name="account_change_password",
    ),
    path(
        "account/password/set/",
        login_required(MyPasswordSetView.as_view()),
        name="account_set_password",
    ),
    
    # All Auth 
    path('account/', include('allauth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)