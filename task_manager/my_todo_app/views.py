from django.shortcuts import render
from django.views.generic.list import ListView
from my_todo_app.models import Task

# Create your views here.
# def home(request):
#     return render(request=request, template_name='home.html')

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
