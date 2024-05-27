
from django.urls import path
from status import views
urlpatterns = [
    path('statuslist/', views.allstatus)
]
