from django.urls import path
from .views import *


urlpatterns = [
    path('get_name/<str:name>',  get_name),
    path('get_surname/<str:surname>',  get_surname),
    path('get_age/<int:age>',  get_age),
    path('get_grade/<int:grade>',  get_grade),
    path('get_phone/<str:phone>',  get_password),
    path('get_email/<str:email>',  get_email),
    path('get_password/<int:password>',  get_password),
]   



