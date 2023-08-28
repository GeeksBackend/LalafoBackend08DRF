from rest_framework import serializers

from apps.categories.models import Category
from apps.posts.serializers import PostSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'parent', 'slug')

class CategoryDetailSerializer(serializers.ModelSerializer):
    category_posts = PostSerializer(read_only=True, many=True)
    class Meta:
        model = Category
        fields = ('id', 'title', 'parent', 'slug', 'category_posts')