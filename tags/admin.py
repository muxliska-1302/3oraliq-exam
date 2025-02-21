from django.contrib import admin

from .models import Tag


class TagInline(admin.StackedInline):
    model = Tag
    extra = 0

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search = ('name',)