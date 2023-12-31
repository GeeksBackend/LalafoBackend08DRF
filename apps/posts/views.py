from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from apps.posts.models import Post, PostComment, PostFavorite
from apps.posts.serializers import PostSerializer, PostCommentSerializer, PostFavoriteSerializer
from apps.posts.permissions import PostPermission

# Create your views here.
class PostAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (IsAuthenticated, )
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'description', 'user', 'category']
    search_fields = ['title', 'description', 'user__username', 'category__title']

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (PostPermission(), )
        return (AllowAny(), )
        
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
class PostCommentAPIView(GenericViewSet,
                         mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (PostPermission(), )
        return (AllowAny(), )
        
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
class PostFavotiteAPIView(GenericViewSet,
                         mixins.CreateModelMixin,
                         mixins.DestroyModelMixin):
    queryset = PostFavorite.objects.all()
    serializer_class = PostFavoriteSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (PostPermission(), )
        return (AllowAny(), )
        
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)