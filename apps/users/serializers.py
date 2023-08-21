from rest_framework import serializers

from apps.users.models import User 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name', 'last_name',
                  'email', 'date_joined', 'profile_image')

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
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            profile_image=validated_data['profile_image']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user