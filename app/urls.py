from django.urls import path
from app.views import *
app_name='something'
urlpatterns=[
    path('first_1/',first_1,name='first_1'),
    path('second_1/',second_1,name='second_1'),
    path('third_1/',third_1,name='third_1'),
]