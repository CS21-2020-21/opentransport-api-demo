from django.urls import include, path
from . import views
from rest_framework import routers



app_name = 'customers'

router = routers.DefaultRouter()
router.register(r'purchase', views.PurchaseViewSet, basename='Purchase')
router.register(r'concession', views.ConcessionViewSet, basename='Concession')
router.register(r'usage', views.UsageViewSet, basename='Usage')


urlpatterns = [
    path('', views.index, name='index'),
    path('delete_user_profile/', views.deactivate_user_view, name='delete_user_profile'),
    path('delete_user/', views.deactivate_user, name='delete_user'),
    path('accounts/', views.my_account, name="my_account"),
    path('accounts/query/', views.query, name="query"),
    path('accounts/change_data/', views.change_data, name="change_data"),
    path('accounts/query/purchases', views.query_purchases, name="query_purchases"),
    path('accounts/query/concessions', views.query_concessions, name="query_concessions"),
    path('accounts/query/usages', views.query_usages, name="query_usages"),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
