# drf_tutorial/memo/serializers.py
from rest_framework import serializers
from .models import Memo


class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memo
        fields = ['id', 'name', 'description', 'is_deleted', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']  # 생성 및 수정 날짜는 읽기 전용

    def validate(self, attrs):
        user = self.context.get("request").user

        if not user or not user.is_authenticated:
            raise serializers.ValidationError("인증되지 않은 사용자입니다.")
        
        validated_data = super().validate(attrs)
        validated_data['user_id'] = user.id

        return validated_data

    # def to_representation(self, instance):
    #     represented = super().to_representation(instance)
    