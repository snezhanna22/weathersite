from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_created')
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']