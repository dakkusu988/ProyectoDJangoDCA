from django.urls import path
from . import views
from .views import TaskView

urlpatterns = [
        path('', TaskView.as_view(), name='TaskViews'),
]