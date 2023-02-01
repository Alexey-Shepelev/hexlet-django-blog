from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.views import View

from .models import Article
from .forms import ArticleForm

# Create your views here.


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
                'articles': articles,
            })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Статья успешно создана.')
            return redirect('articles:index')
        return render(request, 'articles/create.html', {'form': form})


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', {
            'form': form, 'article_id': article_id})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Статья успешно обновлена.')
            return redirect('articles:index')
        return render(request, 'articles/update.html', {
            'form': form, 'article_id': article_id})


class ArticleFormDeleteView(View):

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
            messages.add_message(request, messages.SUCCESS,
                                 'Статья %s успешно удалена.' % article.name)
        return redirect('articles:index')

# def index(request, tags, article_id):
#     return HttpResponse(f'Статья номер {article_id}. Тег {tags}')
