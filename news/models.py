from django.db import models
from django.urls import reverse

class News(models.Model):
    images = models.ImageField(blank=True, null=True, verbose_name='Картинка', upload_to='media', default=None)
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    content = models.TextField(verbose_name='Текст поста')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания поста')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения поста')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

        ordering = ['-time_created']
        indexes = [
            models.Index(fields=['-time_created'])
        ]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('news:post', kwargs={"post_slug": self.slug})
    