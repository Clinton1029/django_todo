from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task, Category
from .forms import TaskForm, CategoryForm
from django.utils import timezone

# Home page (requires login)
@login_required(login_url='login')
def index(request):
    # Optional filters
    q = request.GET.get('q', '')
    category = request.GET.get('category', '')

    tasks = Task.objects.filter(user=request.user)  # Only show tasks for the logged-in user

    if q:
        tasks = tasks.filter(title__icontains=q)

    if category:
        tasks = tasks.filter(category__id=category)

    categories = Category.objects.all().order_by('name')

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # associate task with logged-in user
            task.save()
            return redirect('home')
    else:
        form = TaskForm()

    context = {
        'tasks': tasks,
        'form': form,
        'categories': categories,
        'q': q,
        'current_category': category,
    }
    return render(request, 'index.html', context)


@login_required(login_url='login')
def delete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == "POST":
        task.delete()
    return redirect('home')


@login_required(login_url='login')
def edit_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit.html', {'form': form, 'task': task})


@login_required(login_url='login')
def toggle_complete(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == "POST":
        task.completed = not task.completed
        task.save()
    return redirect('home')


@login_required(login_url='login')
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('home')


# ---------------- Authentication views ----------------

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately
            messages.success(request, "Account created successfully!")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect('login')
