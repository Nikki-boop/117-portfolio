from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

class ProjectsListView(ListView):
    model = Project
    template_name = 'projects/projects_list.html'
    context_object_name = 'projects'

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/projects_new.html'
    success_url = reverse_lazy('projects_list')

