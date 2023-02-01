from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = ['обучение', 'программирование', 'python', 'oop']
        return context


# def index(request):
#     url = reverse(
#         'article',
#         kwargs={'tags': 'python', 'article_id': 42}
#     )
#     return redirect(url)


# def about(request):
#     tags = ['обучение', 'программирование', 'python', 'oop']
#     return render(
#         request,
#         'about.html',
#         context={'tags': tags})
