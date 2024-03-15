from django.shortcuts import render,redirect
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from blog.models import Article
from blog.forms import ArticleForm
from django.urls import reverse_lazy

def dashboard(request):
     return render(request,'bd.html')

def user_article(request):
     if not request.user.is_authenticated:
          return redirect('home')
          
     list_articles = Article.objects.filter(user=request.user)
     return render(request,'my-articles.html',{'list_articles':list_articles})

class AddArticle(CreateView):
     model = Article
     form_class = ArticleForm
     template_name = "add-article.html"
     success_url = reverse_lazy ('my_articles')
     
     def form_valid(self,form):
          form.instance.user = self.request.user
          return super().form_valid(form) 
     
class UpdateArticle(UpdateView):
     model = Article
     form_class = ArticleForm
     template_name = 'app_admin/article_form.html' 
     success_url = reverse_lazy('my_articles')
     
class DeleteArticle(DeleteView):
     model = Article
     success_url = "/my-articles/"
     
      