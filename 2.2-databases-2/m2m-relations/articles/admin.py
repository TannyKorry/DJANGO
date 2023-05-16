from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Rubric, RubricArticles

class RubricArticlesInlineFormset(BaseInlineFormSet):
    def clean(self):
        its_main = 0
        for form in self.forms:
            if self.deleted_forms and self._should_delete_form(form):
                continue
            elif form.cleaned_data.get('is_main'):
                its_main += 1
        if its_main > 1:
            raise ValidationError('Основным может быть только один раздел')
        elif its_main == 0:
            raise ValidationError('Укажите основной раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RubricArticlesInline(admin.TabularInline):
    model = RubricArticles
    formset = RubricArticlesInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    list_filter = ['title']
    inlines = [RubricArticlesInline, ]


@admin.register(Rubric)
class RubricAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
