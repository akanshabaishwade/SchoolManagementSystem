from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('students/', include('apps.students.urls')),
    path('teachers/', include('apps.teachers.urls')),
    path('', include('base_app.urls')),
    path("admin/", admin.site.urls),
    path("", include('admin_datta.urls')),
    path('', include('django_dyn_dt.urls')),
]

