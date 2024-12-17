from django.shortcuts import get_object_or_404, render
from .models import Project

def index(request):

        projects = Project.objects.all().order_by('-completion').filter(is_published=True)

        context = {
            'projects': projects
        }
        return render(request, 'projects/projects.html', context)
    

def project(request, project_id):

        project = get_object_or_404(Project, pk=project_id)

        context = {
            'project': project
        }
        return render(request, 'projects/project.html', context)
    
   