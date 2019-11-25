from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def input(request):
    return render(request, "input.html")


def add(request):
    x = request.GET["t1"]
    y = request.GET["t2"]
    try:
        i = int(x)
        j = int(y)
        k = i + j
        return HttpResponse("<html><body bgcolor=red><h1>sum is:" + str(k) + "</h1></body></html>")
    except ValueError:
        return render(request, "input.html")
