from django.contrib import admin
from django.urls import path

from newspaper.views import index, TopicListView, RedactorListView, ArticleListView, ArticleDetailView, \
    RedactorDetailView, ArticleDeleteView, ArticleUpdateView, ArticleCreateView

urlpatterns = [
    path('', index, name="index"),
    path('topics/', TopicListView.as_view(), name="topic-list"),
    path('articles/', ArticleListView.as_view(), name="article-list"),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name="article-detail"),
    path("articles/create/", ArticleCreateView.as_view(), name="car-create"),
    path("articles/<int:pk>/update/", ArticleUpdateView.as_view(), name="car-update"),
    path("articles/<int:pk>/delete/", ArticleDeleteView.as_view(), name="car-delete"),
    path('redactors/', RedactorListView.as_view(), name="redactor-list"),
    path('redactors/<int:pk>/', RedactorDetailView.as_view(), name="redactor-detail"),
]

app_name = "newspaper"
