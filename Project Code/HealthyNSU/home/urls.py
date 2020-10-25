from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='HealthyNSU-home'),
    path('about/', views.about, name='HealthyNSU-about'),
    path('nearhospital/', views.nearhospital, name='HealthyNSU-nearhospital')
]
