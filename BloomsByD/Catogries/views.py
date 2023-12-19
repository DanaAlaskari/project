from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Category


# Create your views here.
def home( request):
    return render(request, 'home.html',{})
    
def catogries( request):
    Catogries_objects = Category.objects.all()
    return render(request, 'catogries.html',{'Catogries_objects' : Catogries_objects})

def category_details(request, Category_id):
    category_item = Category.objects.get(id=Category_id)
    return render(request, 'view.html', {'Category': Category})


class HomeView(ListView):
    model = Category
    template_name = 'home.html'

class CatogriesView(ListView):
    model = Category
    template_name = 'catogries.html'

class CatogriesDetails(DetailView):
    model = Category
    template_name = 'view.html'
    
class reviewDetails(DetailView):
    model = Category
    template_name = 'add_review.html'