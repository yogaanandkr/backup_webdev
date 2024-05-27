from django.urls import path
from wikipedia import views
urlpatterns = [
    path('', views.wiki, name= 'wiki')
]
