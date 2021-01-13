from django.urls import path
from . import views



app_name = 'customers'

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

]
