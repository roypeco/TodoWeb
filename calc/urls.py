from django.urls import path
from .views import SumNumbers

urlpatterns = [
    path("", SumNumbers.as_view(), name="home"),
]