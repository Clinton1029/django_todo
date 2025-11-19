from django import forms
from .models import Task, Category

class TaskForm(forms.ModelForm):
    due_date = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'due_date']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
