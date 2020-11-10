from django.urls import path

from university.views import get_student_list, get_student_detail

app_name = 'university'

urlpatterns = [
    path('students/', get_student_list, name='student-list'),
    path('students/<int:pk>', get_student_detail, name='student-detail'),
]
