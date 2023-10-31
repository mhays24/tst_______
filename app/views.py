from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

# Create your views here.


def hello_view(request, name):
    contex = {
        "name": name,
        "technologies": ["Django", "Python", "HTML", "CSS", "JavaScript"],
    }
    return render(request, "hello.html", contex)
