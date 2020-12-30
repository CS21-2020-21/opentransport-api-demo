from django.urls import path
from django.contrib import admin
from . import views



app_name = 'operators'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete-user-profile/', views.deactivate_user_view, name='delete-user-profile'),
    path('delete-user/', views.deactivate_user, name='delete-user'),
    path('myaccount/', views.myaccount, name="myaccount"),
    path('myaccount/querydata/', views.querydata, name="querydata"),
    path('myaccount/changedata/', views.changedata, name="changedata"),
    path('myaccount/querydata/viewmodes', views.viewmodes, name="viewmodes"),
    path('myaccount/querydata/viewoperators', views.viewoperators, name="viewoperators"),
]
