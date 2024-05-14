   

from rest_framework import generics
from .models import *
from apps.teachers.models import *
from apps.guardians.models import *
from apps.teachers.serializers import *
from apps.guardians.serializers import *
from apps.students.serializers import *
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count, Sum
from django.utils import timezone
from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response




def important_states_count(request):
    current_year = timezone.now().year
    previous_year = current_year - 1

    # Fetch counts and sums in a single query
    student_counts = Student.objects.aggregate(
        total_students=Count('id'),
        total_students_previous=Count('id', filter=models.Q(created_at__year=previous_year))
    )

    teacher_counts = Teacher.objects.aggregate(
        total_teachers=Count('id'),
        total_teachers_previous=Count('id', filter=models.Q(created_at__year=previous_year))
    )

    award_counts = StudentAchievement.objects.aggregate(
        total_awards=Count('id'),
        total_awards_previous=Count('id', filter=models.Q(created_at__year=previous_year))
    )

    revenue_data = StudentFee.objects.filter(paid_date__year__in=[current_year, previous_year]).values('paid_date__year').annotate(
        total_paid_amount=Sum('paid_amount')
    )

    total_revenue_current = sum(item['total_paid_amount'] for item in revenue_data if item['paid_date__year'] == current_year)
    total_revenue_previous = sum(item['total_paid_amount'] for item in revenue_data if item['paid_date__year'] == previous_year)

    # Calculate growth
    total_students_growth = student_counts['total_students'] - student_counts['total_students_previous']
    total_teachers_growth = teacher_counts['total_teachers'] - teacher_counts['total_teachers_previous']
    total_awards_growth = award_counts['total_awards'] - award_counts['total_awards_previous']
    total_revenue_growth = abs(total_revenue_current - total_revenue_previous)

    # Cap growth at 100%
    total_students_growth = min(total_students_growth, 100)
    total_teachers_growth = min(total_teachers_growth, 100)
    total_awards_growth = min(total_awards_growth, 100)
    total_revenue_growth = min(total_revenue_growth, 100)

    data = {
        'total_students': student_counts['total_students'],
        'total_students_growth': total_students_growth,
        'total_teachers': teacher_counts['total_teachers'],
        'total_teachers_growth': total_teachers_growth,
        'total_awards': award_counts['total_awards'],
        'total_awards_growth': total_awards_growth,
        'total_revenue': total_revenue_current,
        'total_revenue_growth': total_revenue_growth,
    }

    return JsonResponse(data)




def student_overview(request):
    student_counts = Student.objects.values('gender').annotate(count=Count('id')).order_by('id')
    boys_count = student_counts.filter(gender='M').first()['count'] if student_counts.filter(gender='M').exists() else 0
    girls_count = student_counts.filter(gender='F').first()['count'] if student_counts.filter(gender='F').exists() else 0
    complaints_count = Complaint.objects.count()
    # todays_absent_count = StudentAttendance.objects.filter(class_date=date.today(), is_present=False).count()
    absent_count = StudentAttendance.objects.filter(is_present=False).count()
    achievements_count = StudentAchievement.objects.count()

    data = {
        'boys': boys_count,
        'girls': girls_count,
        'complaints': complaints_count,
        'absent': absent_count,
        # 'absent_today': todays_absent_count,
        'achievements': achievements_count
    }
    
    return JsonResponse(data)







def attendance_overview(request):
    DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    # Get the attendance counts for each day of the week
    day_counts = StudentAttendance.objects.values('day').annotate(count=Count('id'))

    # Create a dictionary to hold the counts for each day
    day_count_dict = {day_count['day']: day_count['count'] for day_count in day_counts}

    # Initialize the attendance data with 0 for each day of the week
    attendance_data = [day_count_dict.get(day, 0) for day in DAYS_OF_WEEK]

    # Construct the response data
    data = {
        'days': DAYS_OF_WEEK,
        'attendanceData': attendance_data
    }

    return JsonResponse(data)


def school_events(request):

    school_events = SchoolEvent.objects.all().count()
    data = {
        'school_events':school_events
    }
    return JsonResponse(data)



class AllDataAPIView(APIView):
    def get(self, request):
        students = Student.objects.all()
        teachers = Teacher.objects.all()
        guardians = Guardian.objects.all()
        schoolstaff = SchoolStaff.objects.all()

        student_serializer = StudentSerializer(students, many=True)
        teacher_serializer = TeacherSerializer(teachers, many=True)
        guardian_serializer = GuardianSerializer(guardians, many=True)
        schoolstaff_serializer = SchoolStaffSerializer(schoolstaff, many=True)

        data = {
            'students': student_serializer.data,
            'teachers': teacher_serializer.data,
            'guardians': guardian_serializer.data,
            'schoolstaff': schoolstaff_serializer.data
        }

        return Response(data)

