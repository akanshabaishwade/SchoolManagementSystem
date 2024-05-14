from django.db import models
from base_app.models import *
from base_app.choice import *
from apps.teachers.models import *




class Student(TimeStampedModel):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    address = models.TextField()
    classes = models.ForeignKey(Class, on_delete=models.CASCADE, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="O")
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_enrollment = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name.username



class StudentAttendance(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_date = models.DateField()
    day = models.CharField(max_length=30, choices=Days, default="Monday")
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.name} - {self.class_date}"


class StudentPerformance(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}"


class StudentFee(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classname = models.ForeignKey(Class, on_delete=models.CASCADE,  blank=True, null=True)
    classfee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_amount = models.DecimalField(max_digits=10, decimal_places=2,  blank=True, null=True)
    paid_date = models.DateField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.name} - {self.paid_amount}"


class StudentHealthRecord(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    blood_group = models.CharField(max_length=5)
    medical_history = models.TextField(blank=True)

    def __str__(self):
        return f"Health record of {self.student.name}"


class StudentAchievement(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    achievement_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"Achievement of {self.student.name}"

