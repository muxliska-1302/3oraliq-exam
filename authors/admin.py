from django.contrib import admin

from .models import Author


class AuthorInline(admin.StackedInline):
    model = Author
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo')
    search_fields = ('name',)