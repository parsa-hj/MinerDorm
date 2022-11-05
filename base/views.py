from django.shortcuts import render
from .models import Dorm
from .forms import DormForm

def home(request):
    dorms = Dorm.objects.all()
    context = {'dorms': dorms}
    return render(request, 'base/home.html', context)


def dorms(request, pk):
    dorms = Dorm.objects.get(id=pk)
    context = {'dorms': dorms}
    return render(request, 'base/dorms.html', context)

def writeReview(request):
    form = DormForm()
    context = {'form':form}
    return render(request, 'base/dorms_form.html', context)
