from django.contrib import admin

from .models import Category


class CategoryInline(admin.StackedInline):
    model = Category
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search = ('name',)