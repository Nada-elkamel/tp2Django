from django.urls import path
from .import views

urlpatterns =[
    path('',views.index,name='index'),
]

#py manage.py runserver 8010 (changement de port )
#127.0.0..1:8010/