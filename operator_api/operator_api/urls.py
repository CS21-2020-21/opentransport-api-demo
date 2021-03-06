"""operator_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from api import views

router = DefaultRouter()
router.register(r'cat', views.CatalogueViewSet, basename='catalogue')
router.register(r'operator', views.ItemViewSet, basename='operator')
router.register(r'mode', views.ModeViewSet, basename='mode')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('change_data/', views.change_data, name="change_data"),
    path('accounts/', include('allauth.urls')),
    path(r'', include(router.urls)),
    path(r'', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
