from django.urls import path, include
from .views import *

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('login/',loginMe,name='login'),
    path('signin/', signin, name='signin'),
    path('logout/', logoutPage, name='logout'),
    path('assign/',assign,name='assign'),
    path('code/',code,name='code'),
]