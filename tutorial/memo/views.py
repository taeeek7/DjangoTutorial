# drf_tutorial/memo/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Memo
from .serializers import MemoSerializer

class MemoViewSet(viewsets.ModelViewSet):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 접근 가능

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # 현재 사용자로 메모 생성

    def destroy(self, request, pk=None):
        try:
            memo = self.get_object()
            memo.is_deleted = True  # 삭제 플래그 설정
            memo.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Memo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
