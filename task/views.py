from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views import View

""" Forma anterior sin Class
--------------------------------
def task_list(request):
  
  tasks = Task.objects.all()

  if request.method == 'POST':
    form = TaskForm(request.POST)

    if form.is_valid():
      form.save()
      return redirect('task_list')
    
  else:
    form= TaskForm()
  return render(request, 'task/task_list.html', {'tasks':tasks, 'form':form})
"""

class TaskView(View):

  tasks = Task.objects.all()

  def actualizaTask(self):
    self.tasks = Task.objects.all()
    return self.tasks

  def get(self, request):
    form= TaskForm()
    return render(request, 'task/task_list.html', {'tasks':self.actualizaTask(), 'form':form})
  
  def post(self, request):
    form = TaskForm(request.POST)

    if form.is_valid():
      form.save()
      return redirect('task_list')
  
    return render(request, 'task/task_list.html', {'tasks':self.actualizaTask(), 'form':form})