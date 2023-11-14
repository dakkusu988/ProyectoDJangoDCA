from django import forms

"""
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
"""

class TaskForm(forms.Form):
    title = forms.CharField(label="title", max_length=200)
    description = forms.CharField(label="description", widget=forms.Textarea)
    completed = forms.BooleanField(label="completed", required=False)