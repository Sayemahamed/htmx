from django.shortcuts import render

def index(request):
    return render(request,"base.html");
def users(request):
    return render (request,"users.html")
def alpine_sandbox(request):
    return render (request,"sandbox.html")