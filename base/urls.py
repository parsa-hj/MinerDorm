from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('dorms/<str:pk>/', views.dorms, name="dorms"),
]