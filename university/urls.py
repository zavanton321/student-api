from django.urls import path, include

from university.views import get_student_list

app_name = 'university'

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', get_student_list, name='student-list'),
]
