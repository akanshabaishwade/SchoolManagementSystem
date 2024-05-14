from django.test import TestCase
from apps.students.models import *
from apps.teachers.models import * 
from apps.guardians.models import * 
from base_app.models import * 


from faker import Faker
import random
from random import choice
from random import randint



# run command - python manage.py test apps.students.tests.TestDummyDataCreation

fake = Faker()

class TestDummyDataCreation(TestCase):
    # for _ in range(10):
    #     username = fake.user_name()
    #     email = fake.email()
    #     first_name = fake.first_name()
    #     last_name = fake.last_name()
    #     password = fake.password()
    #     role = choice(['student', 'teacher', 'guardian'])

    #     CustomUser.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,role=role, password=password)

# #----------------------------------------------------------------
 
    # # Create a new CustomUser with faker-generated details and role set to 'teacher'
    # new_teacher = CustomUser.objects.create_user(
    #     username=fake.user_name(),
    #     email=fake.email(),
    #     password=fake.password(),
    #     first_name=fake.first_name(),
    #     last_name=fake.last_name(),
    #     role='teacher'
    # )

    # print(f"Created new teacher: {new_teacher.username}")

    # # Get all users
    # all_users = CustomUser.objects.all()

    # # Print all users
    # for user in all_users:
    #     print(f"Username: {user.username}, Role: {user.role}, Email: {user.email}, Name: {user.first_name} {user.last_name}")

# # ----------------------------------------------------------------

    # # Generate class names from 1 to 12
    # class_names = [f"Class {i}" for i in range(1, 13)]

    # # Get all users with the 'teacher' role
    # teachers = CustomUser.objects.filter(role='teacher')

    # # Check if there are any teachers available
    # if teachers.exists():
    #     # Create Class instances
    #     for name in class_names:
    #         # Select a random user as the class teacher
    #         class_teacher = choice(teachers)

    #         # Create a Class instance
    #         class_instance = Class.objects.create(
    #             name=name,
    #             classteacher=class_teacher
    #         )

    #         print(f"Created class: {class_instance.name} with teacher: {class_teacher.username}")
    # else:
    #     print("No teachers available.")

# #----------------------------------------------------------------
    # from random import choice

    # # Get all users with the 'teacher' role
    # teachers_users = CustomUser.objects.filter(role='teacher')
    # print(teachers_users)

    # # Get all Class instances
    # classes = list(Class.objects.all())

    # # Create or update dummy data for teachers
    # for user in teachers_users:
    #     # Check if a Teacher instance already exists for the user
    #     teacher, created = Teacher.objects.get_or_create(user=user)
    #     if created:
    #         if classes:
    #             teacher.classes_taught.add(choice(classes))
    #             print(f"Created teacher: {teacher} with class: {teacher.classes_taught.first()}")
    #         else:
    #             print(f"No classes available for teacher: {teacher}")
    #     else:
    #         print(f"Teacher already exists for user: {user}")


# ----------------------------------------------------------------------------------------
    # subject_names = [
    #     "Mathematics", "English", "Science", "History", "Geography",
    #     "Physics", "Chemistry", "Biology", "Social Studies", "Computer Science",
    #     "Art", "Music", "Physical Education", "French", "Spanish",
    #     "Literature", "Economics", "Business Studies", "Psychology", "Sociology",
    #     "Health Education"
    # ]

    # # Get all teachers
    # teachers = Teacher.objects.all()

    # # Create subjects with random teachers
    # for name in subject_names:
    #     # Get a random teacher
    #     teacher = random.choice(teachers)

    #     # Create a Subject instance
    #     subject = Subject.objects.create(
    #         name=name,
    #         teacher=teacher
    #     )

    #     print(f"Created subject: {subject}")
# # --------------------------------------------------------------------------------


    # # Get existing records
    # classes = Class.objects.all()
    # teachers = Teacher.objects.all()

    # # Create dummy data for schedules
    # for _ in range(10):  # Create 10 schedules
    #     # Get a random class and teacher
    #     class_instance = random.choice(classes)
    #     teacher = random.choice(teachers)

    #     # Get a random day of the week
    #     day_of_week = random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

    #     # Get a random start time and end time
    #     start_time = fake.time()
    #     end_time = fake.time()

    #     # Create a new schedule
    #     schedule = Schedule.objects.create(
    #         class_name=class_instance,
    #         day_of_week=day_of_week,
    #         start_time=start_time,
    #         end_time=end_time,
    #         teacher=teacher,
    #         notes=fake.text()
    #     )

    #     print(f"Created schedule: {schedule}")
# # --------------------------------------------------------------------------------


    # # Get existing teachers
    # teachers = Teacher.objects.all()

    # # Updated choices for degree and field
    # DEGREE_CHOICES = [
    #     ('BSc', 'Bachelor of Science'),
    #     ('BA', 'Bachelor of Arts'),
    #     ('MSc', 'Master of Science'),
    #     ('MA', 'Master of Arts'),
    #     ('PhD', 'Doctor of Philosophy'),
    #     ('Other', 'Other'),
    # ]

    # FIELD_CHOICES = [
    #     ('Engineering', 'Engineering'),
    #     ('Science', 'Science'),
    #     ('Arts', 'Arts'),
    #     ('Business', 'Business'),
    #     ('Health', 'Health'),
    #     ('Other', 'Other'),
    # ]

    # # Create dummy data for qualifications
    # for _ in range(10):  # Create 10 qualifications
    #     # Get a random teacher
    #     teacher = random.choice(teachers)

    #     # Get a random degree, field, and year completed
    #     degree, degree_full = random.choice(DEGREE_CHOICES)
    #     field, field_full = random.choice(FIELD_CHOICES)
    #     year_completed = fake.random_int(min=1950, max=2022)

    #     # Create a new qualification
    #     qualification = Qualification.objects.create(
    #         teacher=teacher,
    #         degree=degree_full,
    #         field=field_full,
    #         institution=fake.company(),
    #         year_completed=year_completed
    #     )

    #     print(f"Created qualification: {qualification}")

# #--------------------------------------------------------------------------------


    # # Get existing teachers
    # teachers = Teacher.objects.all()

    # # Create dummy data for salaries
    # for _ in range(10):  # Create 10 salaries
    #     # Get a random teacher
    #     teacher = random.choice(teachers)

    #     # Generate a random salary amount
    #     amount = fake.random_int(min=20000, max=100000)

    #     # Generate a random month and year
    #     month = fake.date_time_this_year()

    #     # Create a new salary record
    #     salary = Salary.objects.create(
    #         teacher=teacher,
    #         amount=amount,
    #         month=month
    #     )

    #     print(f"Created salary: {salary}")
# # --------------------------------------------------------------------------------


    # # Get existing teachers
    # teachers = Teacher.objects.all()

    # # Create dummy data for leaves
    # for _ in range(10):  # Create 10 leave records
    #     # Get a random teacher
    #     teacher = random.choice(teachers)

    #     # Generate random start and end dates
    #     start_date = fake.date_between(start_date="-1y", end_date="today")
    #     end_date = fake.date_between(start_date=start_date, end_date="today")

    #     # Generate a random reason for leave
    #     reason = fake.sentence()

    #     # Choose a random status
    #     status = random.choice(['Scheduled', 'Completed', 'Canceled'])

    #     # Create a new leave record
    #     leave = Leave.objects.create(
    #         teacher=teacher,
    #         start_date=start_date,
    #         end_date=end_date,
    #         reason=reason,
    #         status=status
    #     )

    #     print(f"Created leave: {leave}")

# # --------------------------------------------------------------------------------


    # for _ in range(10):
    #     name = fake.name()
    #     role = fake.random_element(elements=('Watchman', 'Principal', 'Librarian', 'Counselor', 'Administrator', 'Other'))
    #     email = fake.email()
    #     phone_number = fake.phone_number()
    #     address = fake.address()

    #     staff = SchoolStaff.objects.create(
    #         name=name,
    #         role=role,
    #         email=email,
    #         phone_number=phone_number,
    #         address=address
    #     )
    #     print(f"Created staff: {staff}")

# # ------------------------------------------------------------------------------------

    # from django.db.utils import IntegrityError


    # # Create new CustomUser instances for students
    # for _ in range(10):
    #     username = fake.user_name()
    #     email = fake.email()
    #     password = fake.password()

    #     # Create CustomUser
    #     user = CustomUser.objects.create_user(username=username, email=email, password=password, role='student')

    #     class_instance, _ = Class.objects.get_or_create(
    #         name=fake.word(),  # Use fake data for class name
    #         # You can't use teacher here because there's no such field in the Class model
    #         defaults={}
    #     )

    #     try:
    #         # Create Student instance
    #         student = Student.objects.create(
    #             name=user,
    #             date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=25),
    #             address=fake.address(),
    #             classes=class_instance,
    #             gender=fake.random_element(elements=("M", "F", "O")),
    #             phone_number=fake.phone_number(),
    #             date_of_enrollment=fake.date_this_decade()
    #         )
    #         print(f"Created student: {student}")
    #     except IntegrityError as e:
    #         print(f"Error creating student: {e}")

#-------------------------------------------------------------------------

    # students = Student.objects.all()

    # # Create dummy data for student attendance
    # for _ in range(20):  # Create 20 attendance records
    #     student = random.choice(students)  # Get a random student

    #     # Create a new attendance record
    #     attendance = StudentAttendance.objects.create(
    #         student=student,
    #         class_date=fake.date_between(start_date="-1y", end_date="today"),  # Random date in the past year
    #         day = 'Monday',
    #         is_present=True # Randomly assign present or absent
    #     )

    #     print(f"Created student attendance: {attendance.student.name} - {attendance.class_date} - Present: {attendance.is_present}")

# # ------------------------------------------------------------------------------------



    # # Get all existing students and subjects
    # students = Student.objects.all()
    # subjects = Subject.objects.all()

    # # Create dummy data for student performance
    # for _ in range(20):  # Create 20 performance records
    #     student = random.choice(students)  # Get a random student
    #     subject = random.choice(subjects)  # Get a random subject

    #     # Create a new performance record
    #     performance = StudentPerformance.objects.create(
    #         student=student,
    #         subject=subject,
    #         marks=random.randint(0, 100)  # Random marks between 0 and 100
    #     )

    #     print(f"Created student performance: {performance.student.name} - {performance.subject.name} - Marks: {performance.marks}")

# # ------------------------------------------------------------------------------------


    # # Get all existing students and classes
    # students = Student.objects.all()
    # classes = Class.objects.all()

    # # Create 10 dummy student fee records
    # for _ in range(10):
    #     student = random.choice(students)
    #     class_instance = random.choice(classes) if classes.exists() else None
    #     amount = random.randint(10000, 20000)  # Generate a random amount
    #     classfee = random.randint(10000, 20000)  # Generate a random amount
    #     paid_date = fake.date_between(start_date="-1y", end_date="today")
    #     is_paid = random.choice([True, False])

    #     student_fee = StudentFee.objects.create(
    #         student=student,
    #         classname=class_instance,
    #         classfee=classfee,
    #         amount=amount,
    #         paid_date=paid_date,
    #         is_paid=is_paid
    #     )

    #     print(f"Created student fee: {student_fee.student.name} - {student_fee.amount}")
# # ----------------------------------------------------------------

    # # Get all existing students
    # students = Student.objects.all()

    # # Create dummy health records for students
    # for student in students:
    #     height = randint(140, 190) / 100  # Assume height in cm
    #     weight = randint(40, 120)  # Assume weight in kg
    #     blood_group = choice(['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
    #     medical_history = fake.paragraph()

    #     health_record = StudentHealthRecord.objects.create(
    #         student=student,
    #         height=height,
    #         weight=weight,
    #         blood_group=blood_group,
    #         medical_history=medical_history
    #     )

    #     print(f"Created health record for {health_record.student.name}")

# # ----------------------------------------------------------------

    # # Get all students
    #     students = Student.objects.all()

    #     # Create dummy data for student achievements
    #     for _ in range(20):  # Create 20 achievements
    #         # Get a random student if available
    #         student = random.choice(students) if students.exists() else None

    #         # Create a new achievement
    #         achievement = StudentAchievement.objects.create(
    #             student=student,
    #             achievement_date=fake.date_this_decade(),
    #             description=fake.sentence()
    #         )

    #         print(f"Created achievement: {achievement.student.name} - {achievement.achievement_date}")


# # ----------------------------------------------------------------

    #   # Get all students
    #     students = Student.objects.all()

    #     # Create dummy data for guardians
    #     for _ in range(20):  # Create 20 guardians
    #         # Get a random student if available
    #         student = random.choice(students) if students.exists() else None

    #         # Create a new guardian
    #         guardian = Guardian.objects.create(
    #             name=fake.name(),
    #             student=student,
    #             relationship_to_student=random.choice(['Parent', 'Sibling', 'Relative']),
    #             email=fake.email(),
    #             phone_number=fake.phone_number(),
    #             occupation=fake.job(),
    #             address=fake.address(),
    #             address_link=fake.url()
    #         )

    #         print(f"Created guardian: {guardian.name}")
# # ----------------------------------------------------------------



        # # Get all students, guardians, and teachers
        students = Student.objects.all()
        guardians = Guardian.objects.all()
        teachers = Teacher.objects.all()

        # # Create dummy data for emergency contacts
        # for _ in range(20):  # Create 20 emergency contacts
        #     # Get a random student if available
        #     student = random.choice(students) if students.exists() else None

        #     # Create a new emergency contact
        #     emergency_contact = EmergencyContact.objects.create(
        #         name=fake.name(),
        #         student=student,
        #         relationship_to_student=random.choice(['Parent', 'Sibling', 'Relative']),
        #         phone_number=fake.phone_number(),
        #         alternate_phone_number=fake.phone_number() if random.random() > 0.5 else None
        #     )

        #     print(f"Created emergency contact: {emergency_contact.name}")

# # ----------------------------------------------------------------

        # # Create dummy data for complaints
        # for _ in range(20):  # Create 20 complaints
        #     # Get a random student, guardian, and teacher if available
        #     student = random.choice(students) if students.exists() else None
        #     guardian = random.choice(guardians) if guardians.exists() else None
        #     teacher = random.choice(teachers) if teachers.exists() else None

        #     # Create a new complaint
        #     complaint = Complaint.objects.create(
        #         student=student,
        #         guardian=guardian,
        #         teacher=teacher,
        #         complaint_type=random.choice(['Academic', 'Behavioral', 'Other']),
        #         description=fake.text(),
        #         status=random.choice(['Pending', 'Resolved', 'Closed'])
        #     )

        #     print(f"Created complaint: {complaint}")    
# # ----------------------------------------------------------------


        # # Get all students, guardians, and teachers
        # students = Student.objects.all()
        # guardians = Guardian.objects.all()
        # teachers = Teacher.objects.all()

        # # Create dummy data for PTMs
        # for _ in range(20):  # Create 20 PTMs
        #     # Get a random student, guardian, and teacher if available
        #     student = random.choice(students) if students.exists() else None
        #     guardian = random.choice(guardians) if guardians.exists() else None
        #     teacher = random.choice(teachers) if teachers.exists() else None

        #     # Create a new PTM
        #     ptm = PTM.objects.create(
        #         guardian=guardian,
        #         student=student,
        #         teacher=teacher,
        #         datetime=fake.date_time_this_year(),
        #         location=fake.address(),
        #         agenda=fake.text(),
        #         status=random.choice(['Scheduled', 'Completed', 'Canceled']),
        #         notes=fake.text() 
        #     )

        #     print(f"Created PTM: {ptm}")
    # pass