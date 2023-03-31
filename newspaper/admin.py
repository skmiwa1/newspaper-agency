from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from newspaper.models import Topic, Article, Redactor

# Register your models here.
admin.site.register(Topic)
admin.site.register(Article)
admin.site.register(Redactor, UserAdmin)
