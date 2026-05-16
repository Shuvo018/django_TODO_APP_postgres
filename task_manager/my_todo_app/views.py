from typing import Any

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from my_todo_app.models import Task
from .form import TaskCreateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'

    def get_context_data(self, **kargs):
        # print(self.request.user)
        # print(self.request.GET.get('task-summary'))
        task_summary = self.request.GET.get('task-summary', None)
        task_list = Task.objects.filter(user = self.request.user)
        if task_summary:
            task_list = task_list.filter(task_summary__icontains=task_summary)
        context = super().get_context_data(**kargs)
        context['task_list'] = task_list
        return context



    
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'task_create.html'
    success_url = '/'
    # def get_success_url(self, **kargs) -> str:
    #     return reverse_lazy('list')
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'task_create.html'
    success_url = '/'

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_create.html'
    success_url = '/'

class UserCreateView(CreateView):
    form_class = UserCreationForm
    model = User
    success_url = '/login/'
    template_name = 'registration/registration.html'
