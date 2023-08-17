from rest_framework.generics import ListCreateAPIView

from apps.users.models import User 
from apps.users.serializers import UserRegisterSerializer

# Create your views here.
class UserAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer