from django.contrib import admin

from .models import Article, Rubric, RubricArticles


class RubricArticlesInline(admin.TabularInline):
    model = RubricArticles
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    list_filter = ['title']


@admin.register(Rubric)
class RubricAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [RubricArticlesInline, ]

