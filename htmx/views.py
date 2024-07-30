from django.shortcuts import render
import random

def index(request):
    return render(request,"base.html");
def users(request):
    return render (request,"users.html")
def alpine_sandbox(request):
    return render (request,"sandbox.html")
def alpine_component(request):
    return render (request,"component.html")
def htmx(request):
    return render(request,"htmx.html")
def convert(request):
    return render(request,"convert.html")
def poll(request):
    return render(request,"convert.html",{
        'count':random.random()*100,
    })
def alpine(request):
    return render(request,"alpine.html")