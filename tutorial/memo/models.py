# drf_tutorial/memo/models.py
from django.db import models
from django.contrib.auth.models import User


class Memo(models.Model):
    id = models.AutoField(primary_key=True)  # ID 필드 (자동 생성)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 사용자 외래키
    name = models.CharField(max_length=255)  # 메모 제목
    description = models.TextField(null=True)  # 메모 내용
    is_deleted = models.BooleanField(default=False)  # 삭제 여부
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 날짜
    updated_at = models.DateTimeField(auto_now=True)  # 수정 날짜

    def __str__(self):
        return self.name