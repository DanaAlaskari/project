from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import User

def home(request):
    return render(request, 'home.html', {})


class loginView(ListView):
    model = User
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('Home')  

class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'Register.html'

    def get_success_url(self):
        return reverse_lazy('Note')  


class NoteView(ListView):
    model = User
    template_name = 'note.html'
