from django.shortcuts import render # 最初これだけ
from django.views.generic.base import TemplateView

# Create your views here.
class SumNumbers(TemplateView):
    template_name = 'calc/home.html'