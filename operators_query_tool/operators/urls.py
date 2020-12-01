from django.urls import path
from . import views



app_name = 'operators'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/',views.signup, name="signup"),
    path('signin/',views.signin, name="signin"),
   
    path('myaccount/', views.myaccount, name="myaccount"),
    path('myaccount/querydata/', views.querydata, name="querydata"),
    path('myaccount/changedata/', views.changedata, name="changedata"),
    path('myaccount/querydata/viewmodes', views.viewmodes, name="viewmodes"),
    path('myaccount/querydata/viewoperators', views.viewoperators, name="viewoperators"),
]
