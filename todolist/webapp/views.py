from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task

def index_view(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        context = {
            'tasks': tasks
        }
        return render(request, 'index.html', context)
    elif request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        created_at = request.POST.get('created_at')
        Task.objects.create(name=name, description=description, created_at=created_at)

        return redirect('index')

def change_status(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.status = "Выполнен"
    task.save()
    return redirect('index')

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'GET':
        return render(request, 'update.html', context = { 'task': task })
    elif request.method == 'POST':
        task.name = request.POST.get('name')
        task.description = request.POST.get('description')
        task.created_at = request.POST.get('created_at')

        task.save()
        return redirect('index')


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('index')


def kill_all(request):
    task = Task.objects.filter(status = "Выполнен")
    task.delete()
    return redirect('index')
