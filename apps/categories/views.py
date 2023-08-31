from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer, CategoryDetailSerializer

# Create your views here.
class CategoryAPIViewSet(GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CategoryDetailSerializer
        return CategorySerializer