from app1.views import *
from django.urls import path
app_name='one'
urlpatterns=[
    path('app1_page/',app1_page,name='app1_page'),
]