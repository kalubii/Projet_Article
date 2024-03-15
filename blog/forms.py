from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category' , 'descript', 'image']
        labels = {'title': 'Titre', 'category': 'Categorie', 'descript':'Description'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'descript': forms.Textarea(attrs={'class': 'form-control','rows':5}),
        }