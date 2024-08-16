from django.urls import path
from .api import *



urlpatterns = [
    #---------------customer------------
    path('customer/post/',CustomerPostApi.as_view(),name='add-Customer'),

]

