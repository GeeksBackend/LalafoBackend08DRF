from rest_framework.routers import DefaultRouter

from apps.posts.views import PostAPIViewSet


router = DefaultRouter()
router.register('post', PostAPIViewSet, 'api_posts')

urlpatterns = router.urls