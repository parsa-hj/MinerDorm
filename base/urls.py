from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('', views.home, name="home"),
    path('dorms/<str:pk>/', views.dorms, name="dorms"),
    path('account/<str:pk>/', views.account, name="account")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)