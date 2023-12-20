from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Review
from .forms import ReviewForm


def home(request):
    return render(request, 'home.html', {})

class Reviews(CreateView):
    model=Review
    form_class=ReviewForm
    template_name='add_review.html'

    def get_success_url(self):
        return reverse_lazy('ReviewList')
    

class ReviewList(ListView):
    model=Review
    template_name='Reviews.html'
