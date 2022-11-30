from django.urls import path
from app2.views import *
app_name='ha'

urlpatterns=[
    path('third/',third,name='third'),
]