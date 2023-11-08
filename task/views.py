from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForms

def task_list(request):
  tasks = Task.objects.all()

  if request.method == 'POST':
    form=TaskForms(request.POST)

    if form.is_valid():
      form.save()
      return redirect('task_list')
    
  else:
    form= TaskForms()
  return render(request, 'task/task_list.html', {'task':tasks, form})