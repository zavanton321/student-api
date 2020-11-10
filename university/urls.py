from django.urls import path

from university.views import StudentListView, StudentDetailView

app_name = 'university'

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>', StudentDetailView.as_view(), name='student-detail'),
]
