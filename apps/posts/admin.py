from django.contrib import admin

from apps.posts.models import Post, PostComment, PostFavorite

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'created')

@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'created')
    search_fields = ('user__username', 'text')
    list_per_page = 20

@admin.register(PostFavorite)
class PostFavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')
    search_fields = ('user__username', 'post__title')