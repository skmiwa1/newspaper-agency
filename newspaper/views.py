from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic

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


class ArticleListView(generic.ListView):
    model = Article
    context_object_name = "article_list"
    template_name = "newspaper/article_list.html"
    paginate_by = 3
    queryset = Article.objects.select_related("topic")


class ArticleDetailView(generic.DetailView):
    model = Article


class RedactorListView(generic.ListView):
    model = Redactor
    context_object_name = "redactor_list"
    template_name = "newspaper/redactor_list.html"
    paginate_by = 3


class RedactorDetailView(generic.DetailView):
    model = Redactor
    queryset = Redactor.objects.all()
