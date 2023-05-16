from django.db import models


class Rubric(models.Model):

    name = models.CharField(max_length=50, verbose_name='Рубрика')

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'

    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    topic = models.ManyToManyField(Rubric, related_name='articles', through='RubricArticles')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class RubricArticles(models.Model):
    tag = models.ForeignKey(Rubric, on_delete=models.CASCADE, related_name='scopes')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(verbose_name='Основной')

    class Meta:
        ordering = ['-is_main', 'tag__name', ]

    def __str__(self):
        return f'{self.tag} {self.article}'