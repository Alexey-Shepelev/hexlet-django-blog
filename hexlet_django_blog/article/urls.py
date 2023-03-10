from django.urls import path
from .views import (
    IndexView,
    ArticleView,
    ArticleFormCreateView,
    ArticleFormEditView,
    ArticleFormDeleteView
)

app_name = 'articles'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:id>/edit/', ArticleFormEditView.as_view(), name='update'),
    path('<int:id>/delete', ArticleFormDeleteView.as_view(), name='delete'),
    path('<int:id>/', ArticleView.as_view(), name='article'),
    path('create/', ArticleFormCreateView.as_view(), name='create'),
]
