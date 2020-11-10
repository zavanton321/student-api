from django.contrib.auth.models import User
from rest_framework import serializers

from university.models import Student


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    registrator = serializers.HyperlinkedRelatedField(
        view_name='university:user-detail',
        many=False,
        read_only=True
    )
    url = serializers.HyperlinkedIdentityField(
        view_name='university:student-detail'
    )
    rnd = serializers.HyperlinkedIdentityField(view_name='university:student-randnum')

    class Meta:
        model = Student
        fields = ['id', 'url', 'first_name', 'last_name', 'grade', 'random_data', 'registrator', 'rnd']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    students = serializers.HyperlinkedRelatedField(
        view_name='university:student-detail',
        many=True,
        read_only=True
    )
    url = serializers.HyperlinkedIdentityField(
        view_name='university:user-detail'
    )

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'students']
