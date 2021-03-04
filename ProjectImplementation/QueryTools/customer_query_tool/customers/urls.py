from django.urls import include, path
from . import views 
from rest_framework import routers

app_name = 'customers'

router = routers.DefaultRouter()
router.register(r'purchase', views.PurchaseViewSet, basename='Purchase')
router.register(r'concession', views.ConcessionViewSet, basename='Concession')
router.register(r'usage', views.UsageViewSet, basename='Usage')

urlpatterns = [
    path('', include(router.urls)),
    path('index', views.index, name='index'),

    path('accounts/', views.my_account, name="my_account"),
    path('accounts/link_account/', views.link_account, name="link_account"),
    path('accounts/check_email/', views.check_email, name="check_email"),
    path('accounts/account_linked/', views.account_linked, name="account_linked"),
    path('accounts/link_failed/', views.link_failed, name="link_failed"),
    path('accounts/linked_accounts/', views.linked_accounts, name="linked_accounts"),
    path('accounts/linked_accounts/<slug:id_slug>/purchases', views.show_linked_account_purchases, name='show_linked_account_purchases'),
    path('accounts/linked_accounts/<slug:id_slug>/concessions', views.show_linked_account_concessions, name='show_linked_account_concessions'),
    path('accounts/linked_accounts/<slug:id_slug>/usages', views.show_linked_account_usages, name='show_linked_account_usages'),
    
    path('accounts/ferry_account/', views.ferry_query_selection, name="ferry_query_selection"),
    path('accounts/ferry_account/ferry_purchases/', views.ferry_purchases, name="ferry_purchases"),
    path('accounts/ferry_account/ferry_concessions/', views.ferry_concessions, name="ferry_concessions"),
    path('accounts/ferry_account/ferry_usages/', views.ferry_usages, name="ferry_usages"),
    
    path('delete_user_profile/', views.delete_user_view, name='delete_user_profile'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('delete_user_failed/', views.delete_user_failed, name='delete_user_failed'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
