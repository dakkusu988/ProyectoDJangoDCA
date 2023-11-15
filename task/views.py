from django.shortcuts import render, redirect, get_object_or_404
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

      titulo = form.cleaned_data['title']
      description = form.cleaned_data['description']
      completed = form.cleaned_data['completed']

      Task.objects.create(title=titulo, description=description, completed=completed)

      #form.save()
      return redirect('task_list')
  
    return render(request, 'task/task_list.html', {'tasks':self.actualizaTask(), 'form':form})
  
class TaskDetailView(View):

  def get(self, request, pk):
    task= get_object_or_404(Task, pk=pk)
    return render(request, 'task/task_detail.html', {'tasks':task})