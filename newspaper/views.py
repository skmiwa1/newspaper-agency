from django.shortcuts import render

from newspaper.models import Redactor, Article, Topic


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

