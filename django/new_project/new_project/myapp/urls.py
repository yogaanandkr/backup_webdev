
from django.urls import path
from myapp import views
urlpatterns = [
    path('home/', views.index)
]
