from django.shortcuts import render

# Create your views here.
def allstatus(request):
    return render(request, 'status.html', {'name': 'anand'})