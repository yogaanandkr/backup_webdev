from django.urls import path
from college import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('careers/', views.careers, name='careers'),
    path('admission/', views.admissions, name='admission'),
]

