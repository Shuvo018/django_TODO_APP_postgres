from typing import Any

from django.shortcuts import render
from django.views.generic.list import ListView
from my_todo_app.models import Task

# Create your views here.
# def home(request):
#     return render(request=request, template_name='home.html')

class TaskListView(ListView):
    model = Task
    task_list = Task.objects.all()
    template_name = 'task_list.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['task_list'] = self.task_list
        return context
    

    