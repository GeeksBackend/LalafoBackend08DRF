from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок"
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='category_parent',
        verbose_name="Подкатегория",
        blank=True, null=True
    )
    slug = models.SlugField(
        verbose_name="Slug категории"
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"