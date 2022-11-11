from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Dorm, Review
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User or Password is incorrect')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/login_register.html', {'form': form})


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    dorms = Dorm.objects.filter(name__contains=q)

    context = {'dorms': dorms}
    return render(request, 'base/home.html', context)


def dorms(request, pk):
    dorms = Dorm.objects.get(id=pk)

    #add review

    if request.method == 'POST' and request.user.is_authenticated:
        rating = request.POST.get('ratings', 3)
        body = request.POST.get('body', '')
        title = request.POST.get('title', '')
        

        review = Review.objects.create(dorm=dorms, user=request.user, rating=rating, body=body, title=title)

        return redirect('dorms', pk=pk)

    context = {'dorms': dorms}
    return render(request, 'base/dorms.html', context)

def account(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user}
    return render(request, 'base/profile.html', context)