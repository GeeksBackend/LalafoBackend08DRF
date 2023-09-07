from rest_framework.routers import DefaultRouter

from apps.posts.views import PostAPIViewSet, PostCommentAPIView, PostFavotiteAPIView


router = DefaultRouter()
router.register('post', PostAPIViewSet, 'api_posts')
router.register('comment', PostCommentAPIView, 'api_comments')
router.register('favorite', PostFavotiteAPIView, 'api_favorites')

urlpatterns = router.urls