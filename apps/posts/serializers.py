from rest_framework import serializers

from apps.posts.models import Post, PostComment, PostFavorite


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = "__all__"

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment 
        fields = "__all__"

class PostFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostFavorite 
        fields = "__all__"