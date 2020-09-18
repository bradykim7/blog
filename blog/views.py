from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView
from .models import Article
from .form import ArticleForm

# Create your views here.

def index(request):
    return render(request, 'blog/index_main.html')

def test(request):
    return render(request, 'blog/index_main.html')


def Article_List(ListView):
    model = Article
    template_name = '.'
    pass


class Create_Article(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/create_article.html'

