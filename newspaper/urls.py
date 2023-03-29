from django.contrib import admin
from django.urls import path

from newspaper.views import index, TopicListView, RedactorListView, ArticleListView

urlpatterns = [
    path('', index, name="index"),
    path('topics/', TopicListView.as_view(), name="topic-list"),
    path('articles/', ArticleListView.as_view(), name="article-list"),
    path('redactors/', RedactorListView.as_view(), name="redactor-list")
]

app_name = "newspaper"
