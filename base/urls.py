from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('dorms/<str:pk>/', views.dorms, name="dorms"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)