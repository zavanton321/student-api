from django.urls import path

from university.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
