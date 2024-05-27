from django.shortcuts import render

# Create your views here.
def showChats(request):
    return render(request,'chats.html', context = {'a': "hello how ARE You", 'b': 500})

def filter(request):
    data = {'a': "Yoga Anand", "b": "yokeshanand762001@gmail.com", "c": "malayalam"}
    return render(request, 'filter.html', data)

def allginja(request):
    data = {"Name": "yoga anand", "Age":22, "Course": "python"}  
    return render(request, 'allginja.html', context = {'data': data})

def aboutme(request):
    return render(request,'aboutme.html')