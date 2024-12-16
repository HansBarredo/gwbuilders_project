from django.shortcuts import render

def index(request):
    return render(request, 'projects/projects.html')

    

def project(request):
    return render(request, 'projects/project.html')

   