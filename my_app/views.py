from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
def projects(request):
    return render(request, 'projects.html')
def resume(request):
    return render(request, 'resume.html')
def contact(request):
    return render(request, 'contact.html')

