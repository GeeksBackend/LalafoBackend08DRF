from rest_framework import serializers

from apps.users.models import User 
from apps.posts.serializers import PostSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name', 'last_name',
                  'email', 'date_joined', 'profile_image')

class UserDetailSerializer(serializers.ModelSerializer):
    user_posts = PostSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',
                  'email', 'date_joined', 'profile_image', 'user_posts')

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=100, write_only=True
    )
    confirm_password = serializers.CharField(
        max_length=100, write_only=True
    )

    class Meta:
        model = User 
        fields = ('username', 'profile_image', 'password', 'confirm_password')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password':'Пароли отличаются'})
        elif attrs['username'] == attrs['password']:
            raise serializers.ValidationError({'password':'Введённый пароль слишком похож на имя пользователя.'})
        elif len(attrs['password']) < 8:
            raise serializers.ValidationError({'password':'Введённый пароль слишком короткий. Он должен содержать как минимум 8 символов.'})
        elif 'qwertyui' in attrs['password'] and '12345678' in attrs['password'] and '87654321' in attrs['password']:
            raise serializers.ValidationError({'password':'Введённый пароль слишком широко распространён. (123, qwertyui, 12345678)'})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            profile_image=validated_data['profile_image']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user