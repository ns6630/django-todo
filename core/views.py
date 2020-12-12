from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from core.forms import TodoForm
from core.models import Todo


class TodoListView(ListView):
    template_name = 'pages/todo_list.html'
    model = Todo
    context_object_name = 'todo_list'
    paginate_by = 5


class TodoDetailView(DetailView):
    template_name = 'pages/todo_detail.html'
    model = Todo
    context_object_name = 'todo'


class TodoCreateView(CreateView):
    template_name = 'pages/todo_create.html'
    model = Todo
    form_class = TodoForm


class TodoUpdateView(UpdateView):
    template_name = 'pages/todo_update.html'
    model = Todo
    form_class = TodoForm


class TodoDeleteView(DeleteView):
    template_name = 'pages/todo_delete.html'
    model = Todo
    context_object_name = 'todo'
    success_url = reverse_lazy('core:list')
