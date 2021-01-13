from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'purchase', views.PurchaseViewSet, basename='Purchase')
router.register(r'concession', views.ConcessionViewSet, basename='Concession')
router.register(r'usage', views.UsageViewSet, basename='Usage')




urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]