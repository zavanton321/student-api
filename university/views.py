from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from university.models import Student
from university.serializers import StudentSerializer


@csrf_exempt
def get_student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(instance=students, many=True)
        return JsonResponse(data=serializer.data, safe=False, status=200)
    elif request.method == 'POST':
        parsed = JSONParser().parse(stream=request)
        serializer = StudentSerializer(data=parsed)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=201)
        else:
            return JsonResponse(data=serializer.errors, status=400)


@csrf_exempt
def get_student_detail(request, pk):
    if request.method == 'GET':
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(instance=student)
        return JsonResponse(data=serializer.data, status=200)
    elif request.method == 'PUT':
        student = get_object_or_404(Student, pk=pk)
        parsed = JSONParser().parse(stream=request)
        serializer = StudentSerializer(instance=student, data=parsed)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=200)
        else:
            return JsonResponse(data=serializer.errors, status=400)
    elif request.method == 'DELETE':
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return HttpResponse(status=204)
