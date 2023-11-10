from django.urls import path
from . import views
from .views import TaskViews

urlpatterns = [
        path('', TaskViews.as_view(), name='TaskViews'),
]