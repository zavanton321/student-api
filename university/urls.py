from django.urls import path

from university.views import StudentViewSet

app_name = 'university'

student_list = StudentViewSet.as_view(
    {
        'get': 'list',
        'post': 'create'
    }
)

student_detail = StudentViewSet.as_view(
    {
        'put': 'update',
        'delete': 'destroy',
        'get': 'retrieve'
    }
)

urlpatterns = [
    path('students/', student_list, name='student-list'),
    path('students/<int:pk>', student_detail, name='student-detail'),
]
