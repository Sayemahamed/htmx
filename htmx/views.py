from django.shortcuts import render

def index(request):
    return render(request,"base.html");
def users(request):
    return render (request,"users.html")
def alpine_sandbox(request):
    return render (request,"sandbox.html")
def htmx(request):
    return render(request,"htmx.html")
def convert(request):
    return render(request,"convert.html")