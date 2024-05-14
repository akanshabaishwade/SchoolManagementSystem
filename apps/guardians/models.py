from base_app.models import *
from base_app.choice import *
from apps.students.models import *
from apps.teachers.models import *





class Guardian(TimeStampedModel):
    name = models.CharField(max_length=255)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    relationship_to_student = models.CharField(max_length=255, choices=RELATIONSHIP_CHOICES)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    occupation = models.CharField(max_length=255)
    address = models.TextField()
    address_link = models.URLField(blank=True)

    def __str__(self):
        return self.name


class EmergencyContact(TimeStampedModel):
    name = models.CharField(max_length=255)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    relationship_to_student = models.CharField(max_length=255, choices=RELATIONSHIP_CHOICES)
    phone_number = models.CharField(max_length=20)
    alternate_phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name


class Complaint(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='complaints')
    guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    complaint_type = models.CharField(max_length=20, choices=COMPLAINT_TYPE_CHOICES)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=COMPLAINT_STATUS_CHOICES,  default='Pending')

    def __str__(self):
        return f"Complaint from {self.guardian.name} regarding {self.student.name}"




# Parent-Teacher Meeting
class PTM(TimeStampedModel):
    guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    location = models.CharField(max_length=255)
    agenda = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"PTM with {self.guardian.name} regarding {self.student.name}"

