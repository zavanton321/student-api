from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from university.models import Student
from university.serializers import StudentSerializer


@api_view(['GET', 'POST'])
def get_student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(instance=students, many=True)
        return Response(data=serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def get_student_detail(request, pk):
    if request.method == 'GET':
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(instance=student)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'PUT':
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
