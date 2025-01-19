from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'year', 'image', 'repository', 'skills']
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Project Name"}),
            "description": forms.Textarea(attrs={"placeholder": "Description"}),
            "year": forms.NumberInput(attrs={"placeholder": "YYYY"}),
            "repository": forms.URLInput(attrs={"placeholder": "GitHub URL"}),
            "image": forms.ClearableFileInput(attrs={"placeholder": "Select an Image"}),
        }