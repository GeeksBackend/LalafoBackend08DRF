from rest_framework.routers import DefaultRouter

from apps.users.views import UserAPIViewSet


router = DefaultRouter()
router.register('user', UserAPIViewSet, 'api_users')

urlpatterns = router.urls