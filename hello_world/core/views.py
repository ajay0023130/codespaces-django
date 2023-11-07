from django.shortcuts import render

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

def First_Hello(request):
    
    return render(request,"first.html")
