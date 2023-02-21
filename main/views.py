from django.shortcuts import render, get_object_or_404
from .models import project
from .models import experience
# Create your views here.

def mainView(request):
    projects = project.objects.all()
    experiences = experience.objects.all()
    return render(request, 'home.html', {'project':project, 'experience':experience})

def render_project(request):
    project = project.objects.all()
    return render(request, 'project.html', {'project':project})

def render_experience(request):
    experience = experience.objects.all()
    return render(request, 'experience.html', {'experience':experience})
