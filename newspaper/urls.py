from django.contrib import admin
from django.urls import path

from newspaper.views import index, TopicListView, RedactorListView, ArticleListView, ArticleDetailView, \
    RedactorDetailView

urlpatterns = [
    path('', index, name="index"),
    path('topics/', TopicListView.as_view(), name="topic-list"),
    path('articles/', ArticleListView.as_view(), name="article-list"),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name="article-detail"),
    path('redactors/', RedactorListView.as_view(), name="redactor-list"),
    path('redactors/<int:pk>/', RedactorDetailView.as_view(), name="redactor-detail"),
]

app_name = "newspaper"
