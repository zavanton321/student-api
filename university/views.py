from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from university.models import Student
from university.serializers import StudentSerializer


@api_view(http_method_names=['GET'])
def api_root(request, format=None):
    students = reverse(viewname='university:student-list', request=request, format=format)
    return Response(
        data={
            'students': students
        }
    )


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
