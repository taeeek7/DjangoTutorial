# tutorial/user/serializers.py
from django.contrib.auth import authenticate
from django.contrib.auth.models import User # django 내부 user 모델 그대로 사용
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer): # 이미 있는 Serializer Model을 쓸거야
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer): # Serializer를 내가 정의할거야
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs): # validate_[xxx] 하면 어떤 필드에 대한 유효성 검증 들어감
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if user is None:
            raise serializers.ValidationError("잘못된 사용자 이름 또는 비밀번호입니다.")
        return user