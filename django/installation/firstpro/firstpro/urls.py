from django.contrib import admin
from django.urls import path
# from firstpro import views
from newapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.fun, name="first")
]
