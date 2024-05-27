from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, './college/home.html')
def about(request):
    return render(request, './college/about.html')
def careers(request):
    return render(request, './college/career.html')
def admissions(request):
    return render(request, './college/admissions.html')