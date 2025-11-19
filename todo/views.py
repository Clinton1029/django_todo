from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Task, Category
from .forms import TaskForm, CategoryForm
from django.utils import timezone

def index(request):
    # Optional filters
    q = request.GET.get('q', '')
    category = request.GET.get('category', '')

    tasks = Task.objects.all()

    if q:
        tasks = tasks.filter(title__icontains=q)

    if category:
        tasks = tasks.filter(category__id=category)

    categories = Category.objects.all().order_by('name')

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
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
    return render(request, 'todo/index.html', context)


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.delete()
    return redirect('home')


def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/edit.html', {'form': form, 'task': task})


def toggle_complete(request, id):
    task = get_object_or_404(Task, id=id)
    # toggle on POST (safer)
    if request.method == "POST":
        task.completed = not task.completed
        # If completed set updated_at etc
        task.save()
    return redirect('home')


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('home')
