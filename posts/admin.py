from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_content', 'author', 'category', 'image', 'posted_at')
    list_filter = ('category', 'author', 'tags')
    search_fields = ('title', 'short_content')
    prepopulated_fields = {'slug': ('title',)}
