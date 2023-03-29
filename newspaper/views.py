from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from newspaper.forms import TopicSearchForm
from newspaper.models import Redactor, Article, Topic


@login_required
def index(request):
    num_redactors = Redactor.objects.count()
    num_articles = Article.objects.count()
    num_topics = Topic.objects.count()

    # num_visits = request.session.get("num_visits", 0)
    # request.session["num_visits"] = num_visits + 1

    context = {
        "num_redactors": num_redactors,
        "num_articles": num_articles,
        "num_topics": num_topics
    }

    return render(request, "newspaper/index.html", context=context)


class TopicListView(generic.ListView):
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


class ArticleListView(generic.ListView):
    model = Article
    context_object_name = "article_list"
    template_name = "newspaper/article_list.html"
    paginate_by = 3
    queryset = Article.objects.select_related("topic")


class ArticleDetailView(generic.DetailView):
    model = Article


class ArticleCreateView(generic.CreateView):
    model = Article
    fields = "__all__"
    success_url = reverse_lazy("newspaper:article-list")


class ArticleUpdateView(generic.UpdateView):
    model = Article
    fields = "__all__"
    success_url = reverse_lazy("newspaper:article-list")


class ArticleDeleteView(generic.DeleteView):
    model = Article
    success_url = reverse_lazy("newspaper:article-list")


class RedactorListView(generic.ListView):
    model = Redactor
    context_object_name = "redactor_list"
    template_name = "newspaper/redactor_list.html"
    paginate_by = 3


class RedactorDetailView(generic.DetailView):
    model = Redactor
    queryset = Redactor.objects.all()
