from django.shortcuts import HttpResponse, render

# def index(request):
#     a = open(r"/home/yoga-anand/dev/psp/django/new_project/new_project/templates/index.html", "r")
#     # a = open("../templates/index.html", "r")
#     data = a.read()
#     print(data)
#     return HttpResponse(data)


def index(request):
    return render(request, 'index.html')