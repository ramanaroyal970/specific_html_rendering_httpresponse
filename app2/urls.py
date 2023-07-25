from django.urls import path
from app2.views import *
app_name='something'
urlpatterns=[
    path('first_3/',first_3,name='first_3'),
    path('second_3/',second_3,name='second_3'),
    path('third_3/',third_3,name='third_3'),
]