from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from newspaper.forms import TopicSearchForm, RedactorSearchForm, ArticleSearchForm
from newspaper.models import Redactor, Article, Topic


@login_required
def index(request):
    num_redactors = Redactor.objects.count()
    num_articles = Article.objects.count()
    num_topics = Topic.objects.count()

    context = {
        "num_redactors": num_redactors,
        "num_articles": num_articles,
        "num_topics": num_topics
    }

    return render(request, "newspaper/index.html", context=context)


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "newspaper/topic_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(TopicListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        contex["search_form"] = TopicSearchForm(
            initial={"name": name}
        )
        return contex

    def get_queryset(self):
        queryset = Topic.objects.all()
        form = TopicSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class ArticleListView(LoginRequiredMixin, generic.ListView):
    model = Article
    context_object_name = "article_list"
    template_name = "newspaper/article_list.html"
    paginate_by = 3
    queryset = Article.objects.select_related("topic")

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(ArticleListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        contex["search_form"] = ArticleSearchForm(
            initial={"title": title}
        )
        return contex

    def get_queryset(self):
        queryset = Article.objects.all()
        form = ArticleSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                title__icontains=form.cleaned_data["title"]
            )
        return queryset


class ArticleDetailView(LoginRequiredMixin, generic.DetailView):
    model = Article


class ArticleCreateView(LoginRequiredMixin, generic.CreateView):
    model = Article
    fields = "__all__"
    success_url = reverse_lazy("newspaper:article-list")


class ArticleUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Article
    fields = "__all__"
    success_url = reverse_lazy("newspaper:article-list")


class ArticleDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Article
    success_url = reverse_lazy("newspaper:article-list")


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    context_object_name = "redactor_list"
    template_name = "newspaper/redactor_list.html"
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(RedactorListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        contex["search_form"] = TopicSearchForm(
            initial={"username": username}
        )
        return contex

    def get_queryset(self):
        queryset = Redactor.objects.all()
        form = RedactorSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    queryset = Redactor.objects.all()
