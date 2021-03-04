from django.urls import path

from . import views

app_name = 'operators'

urlpatterns = [
    path('', views.index, name='index'),
    
    path('accounts/', views.my_account, name="my_account"),
    path('accounts/query/', views.query, name="query"),
    path('accounts/change_data/', views.change_data, name="change_data"),
    path('accounts/query/modes', views.query_modes, name="query_modes"),
    path('accounts/query/operators', views.query_operators, name="query_operators"),
    path('accounts/query/operators/operator_pages', views.view_operators, name="view_operators"),

    path('delete-user-profile/', views.deactivate_user_view, name='delete-user-profile'),
    path('delete-user/', views.deactivate_user, name='delete-user'),
]
