from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from university.models import Student
from university.serializers import StudentSerializer


class HomeView(TemplateView):
    template_name = 'university/home.html'


@csrf_exempt
def get_student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(instance=students, many=True)
        return JsonResponse(data=serializer.data, safe=False)
    elif request.method == 'POST':
        pass
