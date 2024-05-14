from django.urls import path
from .views import *

urlpatterns = [
    path('total_students/', important_states_count, name='total_students'),
    path('student_overview/', student_overview, name='total_students'),
    path('attendance_overview/', attendance_overview, name='total_students'),
    path('school_events/', school_events, name='total_students'),
    path('all_data/', AllDataAPIView.as_view(), name='all_data'),


    

    

]
