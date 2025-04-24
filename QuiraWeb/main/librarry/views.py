from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Author
from django.urls import reverse_lazy

class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')  # Redirect to login page on success

    def form_valid(self, form):
        # You can override this method if you need extra logic when the form is valid
        return super().form_valid(form)
class AuthorList(ListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'authors'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'author'

class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author_form.html'
    fields = ['name', 'bio', 'date_of_birth', 'date_of_death']


class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'author_form.html'
    fields = ['name', 'bio', 'date_of_birth', 'date_of_death']


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author_confirm_delete.html'
    success_url = reverse_lazy('author_list')
