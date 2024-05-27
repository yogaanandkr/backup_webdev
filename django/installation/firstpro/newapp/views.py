from django.shortcuts import HttpResponse
from django.shortcuts import render

def fun(request):
    return render(request,'index.html')