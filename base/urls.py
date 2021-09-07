from django.conf.urls import url 
from django.urls import path
from .views import *

app_name = 'base'
 
urlpatterns = [ 
    path('', index, name='index'),
    path('predict', predict, name='predict')
]