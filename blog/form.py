# USAGE admin.py / forms.py
from django import forms
from .models import Article, Category

choices = Category.objects.all().values_list('name', 'name')


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'author',
            'title',
            'contents',
            'category',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'})
        }
