from django.conf import settings

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Topic(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self) -> str:
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(default=0)

    class Meta:
        ordering = ["username"]
        verbose_name = "redactor"
        verbose_name_plural = "redactors"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("newspaper:redactor-detail", kwargs={"pk": self.pk})


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    topic = models.ForeignKey(to=Topic, on_delete=models.CASCADE)
    publishers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="articles")

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("newspaper:article-detail", kwargs={"pk": self.pk})
