from django.shortcuts import render
from .models import Article

def home(request):
    list_articles = Article.objects.all()
    context = {"liste_articles":list_articles}
    return render(request,"index.html",context)

def detail(request,id_article):
    article = Article.objects.get(id=id_article)
    category = article.category
    article_en_relation = Article.objects.filter(category=category)[:7]
    return render(request,'detail.html',{"article":article, "aer":article_en_relation})   

def search(request):
    query = request.GET["article"]
    liste_article = Article.objects.filter(title__icontains=query)
    return render(request,"search.html",{"liste_article":liste_article}) 
