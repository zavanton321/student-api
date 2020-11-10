from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, renderers
from rest_framework.decorators import action
from rest_framework.response import Response

from university.models import Student
from university.permissions import IsRegistrator
from university.serializers import StudentSerializer, UserSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsRegistrator
    ]

    @action(detail=True)
    def randnum(self, request, *args, **kwargs):
        rnd = self.get_object().random_data
        return Response(data=rnd)

    def perform_create(self, serializer):
        serializer.save(registrator=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
