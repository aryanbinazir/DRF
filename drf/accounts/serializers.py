from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'validators': [UniqueValidator(queryset=User.objects.all(),
                                                    message='This email is exist')]}
        }

    def create(self, validated_data):
        del validated_data['password2']
        return User.objects.create_user(**validated_data)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Passwords must be match')
        return data

    # def validate_email(self, value):
    #     user = User.objects.filter(email=value)
    #     if user:
    #         raise serializers.ValidationError('This email is exist')
    #     return value

    # def validate_username(self, value):
    #     user = User.objects.filter(username=value)
    #     if user:
    #         raise serializers.ValidationError('This username is exist')
    #     return value

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'