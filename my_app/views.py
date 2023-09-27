from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello world")
def about(request):
    return HttpResponse("about me")
def hello(request, first_name):
    return HttpResponse('Hello '+first_name)