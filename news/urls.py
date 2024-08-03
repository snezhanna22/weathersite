from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('news/', views.show_all_news, name='show_news'),
    path('news/<slug:post_slug>/', views.show_post, name='post')
]
