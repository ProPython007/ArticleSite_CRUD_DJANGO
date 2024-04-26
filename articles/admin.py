from django.contrib import admin

# Register your models here.
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']
    search_fields = ['title']
    readonly_fields = ['timestamp', 'updated']

admin.site.register(Article, ArticleAdmin)