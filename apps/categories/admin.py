from django.contrib import admin

from apps.categories.models import Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'slug')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug':('title',)}