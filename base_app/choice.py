RELATIONSHIP_CHOICES = (
    ('Parent', 'Parent'),
    ('Sibling', 'Sibling'),
    ('Relative', 'Relative'),
    ('Guardian', 'Guardian'),
    ('Other', 'Other'),
)

DEGREE_CHOICES = [
    ('BSc', 'Bachelor of Science'),
    ('BA', 'Bachelor of Arts'),
    ('MSc', 'Master of Science'),
    ('MA', 'Master of Arts'),
    ('PhD', 'Doctor of Philosophy'),
    ('Other', 'Other'),
]

FIELD_CHOICES = [
    ('Engineering', 'Engineering'),
    ('Science', 'Science'),
    ('Arts', 'Arts'),
    ('Business', 'Business'),
    ('Health', 'Health'),
    ('Other', 'Other'),
]

DAY_CHOICES = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
]

STATUS_CHOICES = (
    ('Scheduled', 'Scheduled'),
    ('Completed', 'Completed'),
    ('Canceled', 'Canceled'),
)

ROLE_CHOICES = (
    ('Watchman', 'Watchman'),
    ('Principal', 'Principal'),
    ('Librarian', 'Librarian'),
    ('Counselor', 'Counselor'),
    ('Administrator', 'Administrator'),
    ('Other', 'Other'),
)

COMPLAINT_TYPE_CHOICES = (
    ('Academic', 'Academic'),
    ('Behavioral', 'Behavioral'),
    ('Other', 'Other'),
)


COMPLAINT_STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    )


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

Days = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)
