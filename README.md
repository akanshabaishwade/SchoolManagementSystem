# School Management System

A comprehensive Django-based web application for efficiently managing schools, students, teachers, and administrative tasks. This project is designed to streamline school operations and enhance communication between stakeholders.

## Features

### User Management
- **Custom User Model**: Manage students, teachers, and administrators with tailored permissions and authentication.
- **Role-based Access Control**: Ensure appropriate permissions based on user roles (admin, teacher, student, parent).

### Design
- **Responsive Design**: Seamlessly experience across devices (desktops, tablets, smartphones).

### Guardian & Complaint Management
- **Guardian Information**: Manage guardian details, including emergency contacts.
- **Complaint Handling**: Students and guardians can file complaints, administrators can efficiently track and manage them.

### Parent-Teacher Meetings (PTM)
- **Scheduling**: Facilitate PTM scheduling and management, improving communication between teachers and parents.

### Teacher Management
- **Information Management**: Manage teacher details, qualifications, salary, and leave requests.

### Student Records
- **Attendance & Performance**: Track student attendance and academic performance.
- **Fees & Health Records**: Manage student fee payments and health records.
- **Achievements**: Record and track student achievements.

### School Staff Management
- **Staff Information**: Manage information of all school staff, ensuring efficient personnel management.

### Event Management
- **Organization**: Organize and manage school events, enhancing the overall school experience.


## Demo

Check out the live demo [here](https://akanshabaishwade.pythonanywhere.com/).

## Login Credentials

- **Username:** admin
- **Password:** admin

## Models

### Core App

| Model Name            | Description                                      |
|-----------------------|--------------------------------------------------|
| CustomUser            | Custom user model with roles for different users |
| TimeStampedModel      | Abstract base model with timestamp fields       |

### Base App

| Model Name            | Description                                      |
|-----------------------|--------------------------------------------------|
| Role                  | Role definition for users                        |
| Permission            | Permission definition for roles                  |

### Students App

| Model Name            | Description                                      |
|-----------------------|--------------------------------------------------|
| Student               | Information about students                       |
| StudentAttendance     | Student attendance records                       |
| StudentPerformance    | Student academic performance records             |
| StudentFee            | Student fee payment records                      |
| StudentHealthRecord   | Student health records                           |
| StudentAchievement    | Student achievements                             |

### Teachers App

| Model Name            | Description                                      |
|-----------------------|--------------------------------------------------|
| Teacher               | Information about teachers                       |
| Qualification         | Teacher's qualifications                         |
| Salary                | Salary details for teachers                      |
| Leave                 | Leave requests and approvals for teachers        |
| SchoolStaff           | Other staff members working in the school        |
| SchoolEvent           | Events organized by the school                   |

### Guardians App

| Model Name            | Description                                      |
|-----------------------|--------------------------------------------------|
| Guardian              | Information about the student's guardian         |
| EmergencyContact      | Emergency contact details for a student          |
| Complaint             | Complaints filed by students or guardians        |
| PTM                   | Parent-Teacher Meeting details                   |


## Installation

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run migrations using `python manage.py migrate`.
4. Create a superuser using `python manage.py createsuperuser`.
5. Start the development server using `python manage.py runserver`.


## Contact

For inquiries or collaboration opportunities, please contact [akanshabaishwade@gmail.com](mailto:akanshabaishwade@gmail.com).

Phone: 7471176966

LinkedIn: [Akansha Baishwade](https://www.linkedin.com/in/akansha-baishwade/)


