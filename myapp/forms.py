from django import forms

# forms.py
from django import forms
from .models import Project, Task

class CreateNewTask(forms.Form):
    """
    Form for creating a new task.
    - title: Text field for the task title.
    - description: Text area for the task description.
    - project: Dropdown for selecting a project.
    """
    title = forms.CharField(
        label="Task Title:",
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'input'})
    )
   
    description = forms.CharField(
        label="Task Description:",
        widget=forms.Textarea(attrs={'class': 'input'})
    )

    project = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        label="Select Project:",
        widget=forms.Select(attrs={'class': 'input'})
    )


class CreateNewProject(forms.Form):
    """
    Form for creating a new project.
    - name: Text field for the project name.
    """
    name = forms.CharField(
        label="Project Name:",
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'input'})
    )
