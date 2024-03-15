"""
URL configuration for my_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import home,detail,search
from app_authenti.views import login_blog,register,logout
from app_admin.views import dashboard,user_article,AddArticle,UpdateArticle,DeleteArticle
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_blog,name="login"),
    path('home/', home,name="home"),
    path('article/<int:id_article>/',detail,name="detail"),
    path('article/recherche/',search,name="search"),
    path('register/',register,name="register"),
    path('logout/',logout,name="logout"),
    path('dashboard/',dashboard,name="dashboard"),
    path('my-articles/', user_article, name='my_articles'), 
    #path('user_article/',user_article,name="user_article"),
    path('ajouter-article/',AddArticle.as_view(),name='ajouter_article'),
    path('my-articles/update-article/<int:pk>/',UpdateArticle.as_view(),name='update_article'),
    path('my-articles/delete-article/<int:pk>/',DeleteArticle.as_view(),name='delete_article'),
    path('authenti/',include('app_authenti.urls')),
    
    #path('admin/',include('app_admin.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#http://127.0.0.1:8000/article/3 => detail(request,id_article=3)