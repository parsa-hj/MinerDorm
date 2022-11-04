from django.shortcuts import render
from .models import Dorm

def home(request):
    dorms = Dorm.objects.all()
    context = {'dorms': dorms}
    return render(request, 'base/home.html', context)


def dorms(request, pk):
    dorms = Dorm.objects.get(id=pk)
    context = {'dorms': dorms}
    return render(request, 'base/dorms.html', context)
