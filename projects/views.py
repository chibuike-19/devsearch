from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return render(request, "index.html", {"name": "Emmanuel"})

def project(request, pk):
    return HttpResponse("Stay right there" + " " + pk)
