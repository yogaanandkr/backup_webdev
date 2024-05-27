from django.urls import path
from chats import views
urlpatterns = [
    path("", views.showChats),
    path("filter/", views.filter),
    path("allginja/", views.allginja), 
    path('aboutme/', views.aboutme, name='aboutme')
]

