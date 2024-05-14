from django.urls import path
from .views import *

urlpatterns = [
    path('teacher_leaves/', LeaveList.as_view(), name='teacher_leaves'),
]
