from django.shortcuts import render
from projects.models import Project

def index(request):
    projects = Project.objects.order_by('-completion').filter(is_published=True)[:3]

    context = {
        'projects': projects
    }
    return render(request, 'pages/index.html', context)