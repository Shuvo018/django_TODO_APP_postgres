# Django Class-Based View TODO App (PostgreSQL)

A TODO application built with Django using **Class-Based Views (CBV)** and PostgreSQL as the database backend.

---

## Class-Based Views

All views live in `task_manager/my_todo_app/views.py` and are wired up in `task_manager/task_manager/urls.py`.

---

### `TaskListView`

Displays all tasks.

```python
from django.views.generic.list import ListView

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
```

| URL Pattern | URL Name | Method |
|-------------|----------|--------|
| `/` | `list` | GET |

```python
path('', view=TaskListView.as_view(), name='list')
```

---

### `TaskCreateView`

Renders a form to create a new task and saves it on submission.

```python
from django.views.generic.edit import CreateView

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'task_create.html'
    success_url = '/'
```

| URL Pattern | URL Name | Method |
|-------------|----------|--------|
| `/create/` | `create` | GET / POST |

```python
path('create/', view=TaskCreateView.as_view(), name='create')
```

---

### `TaskUpdateView`

Renders a pre-filled form to edit an existing task identified by its primary key.

```python
from django.views.generic.edit import UpdateView

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'task_create.html'
    success_url = '/'
```

| URL Pattern | URL Name | Method |
|-------------|----------|--------|
| `/update/<int:pk>` | `update` | GET / POST |

```python
path('update/<int:pk>', view=TaskUpdateView.as_view(), name='update')
```

---

### `TaskDeleteView`

Deletes a task identified by its primary key.

```python
from django.views.generic.edit import DeleteView

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_create.html'
    success_url = '/'
```

| URL Pattern | URL Name | Method |
|-------------|----------|--------|
| `/delete/<int:pk>` | `delete` | POST |

```python
path('delete/<int:pk>', view=TaskDeleteView.as_view(), name='delete')
```

---

## URL Summary

| URL | View Class | Name | Action |
|-----|------------|------|--------|
| `/` | `TaskListView` | `list` | List all tasks |
| `/create/` | `TaskCreateView` | `create` | Create a new task |
| `/update/<int:pk>` | `TaskUpdateView` | `update` | Update an existing task |
| `/delete/<int:pk>` | `TaskDeleteView` | `delete` | Delete a task |
