from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, View, DeleteView, UpdateView
from django.contrib.auth import login
from django.urls import reverse_lazy
from .models import User, Task
from django.shortcuts import get_object_or_404, render, redirect
from .form import UserForm

class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('task_list')
        form = UserForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = UserForm(data=request.POST)
        if not form.is_valid():
            return render(request, 'login.html', {'form': form})
        user = form.get_user()
        login(request, user)
        return redirect('task_list') 

class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    fields = ['user_name', 'nama', 'last_nama', 'email', 'number', 'gender']
    template_name = 'user_create.html'
    login_url = 'login'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

    def get_success_url(self):
        return reverse_lazy('user_list')

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['task_name', 'task_desc', 'date', 'clock']
    template_name = 'create_task.html'
    login_url = 'login'

    def form_valid(self, form):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        form.instance.user = user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user_tasks', kwargs={'user_id': self.kwargs['user_id']})

class ListOfTasks(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'list_of_task.html'
    context_object_name = 'tasks'
    login_url = 'login'

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'
    login_url = 'login'

class MarkTaskDone(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'confirm_delete.html'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('task_list')

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['task_name', 'task_desc', 'date', 'clock']
    template_name = 'update_task.html'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('task_list')
