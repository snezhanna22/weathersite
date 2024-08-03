from django.apps import AppConfig


class NewsConfig(AppConfig):
    verbose_name = 'Новости'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'
