from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Task title (e.g., Complete Django project)',
                'class': 'input'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Short description (optional)',
                'class': 'textarea'
            }),
            'category': forms.Select(attrs={
                'class': 'select'
            }),
            'due_date': forms.DateTimeInput(attrs={
                'placeholder': 'YYYY-MM-DD HH:MM',
                'type': 'datetime-local',
                'class': 'input'
            }),
        }
