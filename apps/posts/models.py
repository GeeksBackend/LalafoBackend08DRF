from django.db import models
from django.contrib.auth import get_user_model

from apps.categories.models import Category

User = get_user_model()

# Create your models here. Django ORM
class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='user_posts',
        verbose_name="Пользователь"
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        related_name='category_posts',
        verbose_name="Категория",
        blank=True, null=True
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to='posts/',
        verbose_name="Фотография"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"