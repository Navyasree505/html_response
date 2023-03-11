from app2.views import *
from django.urls import path
app_name='two'
urlpatterns=[
    path('app2_page/',app2_page,name='app2_page'),
    path('app1_page/',app1_page,name='app1_page'),
]