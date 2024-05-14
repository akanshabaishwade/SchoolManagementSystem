from django.db import models
from base_app.models import *
from base_app.choice import *



class Teacher(TimeStampedModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    classes_taught = models.ManyToManyField('Class', related_name='teachers')

    def __str__(self):
        return self.user.username


class Subject(TimeStampedModel):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name='subjects_taught')
    

    def __str__(self):
        return self.name


class Class(TimeStampedModel):
    name = models.CharField(max_length=100)
    classteacher = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='classes_taught', blank=True, null=True)
    

    def __str__(self):
        return self.name


class Schedule(TimeStampedModel):
    class_name = models.ForeignKey(
        Class, on_delete=models.CASCADE, related_name='schedules')
    day_of_week = models.CharField(max_length=10, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_number = models.CharField(max_length=10, blank=True, null=True)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, blank=True, null=True, related_name='schedules')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.class_name} - {self.get_day_of_week_display()} - {self.start_time}-{self.end_time}"


class Qualification(TimeStampedModel):

    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name='qualifications')
    degree = models.CharField(max_length=100, choices=DEGREE_CHOICES, default='Other')
    field = models.CharField(max_length=100, choices=FIELD_CHOICES, default='Other')
    institution = models.CharField(max_length=100)
    year_completed = models.IntegerField()

    def __str__(self):
        return f"{self.degree} in {self.field} from {self.institution} ({self.year_completed})"


class Salary(TimeStampedModel):
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name='salaries')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField()

    def __str__(self):
        return f"{self.teacher.user.username} - {self.amount} - {self.month}"


class Leave(TimeStampedModel):
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name='leaves')
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.teacher.user.username} - {self.start_date} to {self.end_date} ({self.status})"


class SchoolStaff(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.role}"
    

class SchoolEvent(TimeStampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title