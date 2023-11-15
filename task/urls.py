from django.urls import path
from . import views
from .views import TaskView, TaskDetailView

urlpatterns = [
        path('', TaskView.as_view(), name='TaskViews'),
        path('task/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
]