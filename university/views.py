from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from rest_framework.parsers import JSONParser

from university.models import Student
from university.serializers import StudentSerializer


class HomeView(TemplateView):
    template_name = 'university/home.html'


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



