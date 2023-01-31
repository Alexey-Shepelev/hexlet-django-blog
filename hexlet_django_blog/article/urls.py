from django.urls import path
from .views import IndexView, ArticleView, AticleFormCreateView

app_name = 'articles'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:id>/', ArticleView.as_view(), name='article'),
    path('create/', AticleFormCreateView.as_view(), name='create'),
]
