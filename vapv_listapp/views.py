from django.shortcuts import render
from django.http import HttpResponse

def lista(request):
    return HttpResponse(
        "<h1>hola</h1>"
    )


