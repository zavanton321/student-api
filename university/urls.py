from django.urls import path, include
from rest_framework import routers

from university.views import StudentViewSet, UserViewSet

app_name = 'university'

router = routers.DefaultRouter()
router.register(prefix=r'students', viewset=StudentViewSet)
router.register(prefix=r'users', viewset=UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]
