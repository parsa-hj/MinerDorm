from django.shortcuts import render, redirect
from .models import Dorm, Review
from .forms import DormForm

def home(request):
    dorms = Dorm.objects.all()
    context = {'dorms': dorms}
    return render(request, 'base/home.html', context)


def dorms(request, pk):
    dorms = Dorm.objects.get(id=pk)

    #add review

    if request.method == 'POST':
        rating = request.POST.get('ratings', 3)
        body = request.POST.get('body', '')
        title = request.POST.get('title', '')
        

        review = Review.objects.create(dorm=dorms, user=request.user, rating=rating, body=body, title=title)

        return redirect('dorms', pk=pk)

    context = {'dorms': dorms}
    return render(request, 'base/dorms.html', context)