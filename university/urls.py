from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from university.views import StudentViewSet, api_root

app_name = 'university'

# router = routers.DefaultRouter()
# router.register(prefix=r'students', viewset=StudentViewSet)

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
    path('', api_root),
    path('students/', student_list, name='student-list'),
    path('students/<int:pk>', student_detail, name='student-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
