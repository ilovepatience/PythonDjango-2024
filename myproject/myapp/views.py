from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm
from .forms import CommentForm


def page1(request):
    return HttpResponse("<h1>Головна сторінка</h1><a href='/aboutpage/'>Перейти на інформаційну сторінку    </a>")


def page2(request):
    return HttpResponse("<h1>Інформаційна сторінка</h1><a href='/mainpage/'>Перейти на головну сторінку</a>")


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'myapp/article_list.html', {'articles': articles})


def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'myapp/article_form.html', {'form': form})


def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'myapp/article_confirm_delete.html', {'article': article})


def edit_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', id=article.id)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'edit_article.html', {'form': form})


def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    comments = article.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article_detail', id=article.id)
    else:
        comment_form = CommentForm()

    return render(request, 'article_detail.html', {'article': article, 'comments': comments, 'comment_form': comment_form})
