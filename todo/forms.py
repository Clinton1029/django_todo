from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task, Category


# ---------------------------------------------------------
#  CUSTOM SIGNUP FORM (username, email, password1, password2)
# ---------------------------------------------------------
class CustomSignupForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "placeholder": "Email address",
            "class": "input"
        })
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Username",
            "class": "input"
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Create password",
            "class": "input"
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Confirm password",
            "class": "input"
        })
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# ---------------------------------------------------------
#  TASK FORM
# ---------------------------------------------------------
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'due_date']

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Task title',
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


# ---------------------------------------------------------
#  CATEGORY FORM
# ---------------------------------------------------------
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'New category name',
                'class': 'input'
            })
        }
