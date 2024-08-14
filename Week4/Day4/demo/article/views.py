from django.shortcuts import render, redirect
from .models import Article2

def article_list(request):
    articles = Article2.objects.all()
    return render(request, 'home.html', {'articles': articles})

def add_article(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        print(title,content,author)
        new_article = Article2.objects.create(title=title, content=content, author=author)
        new_article.save()
        return redirect(article_list)

    return render(request, 'add.html')
