from django.contrib import admin
from .models import Memo

class MemoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'is_deleted', 'created_at', 'updated_at')  # 목록에서 보여줄 필드
    list_filter = ('is_deleted', 'user')  # 필터링 옵션
    search_fields = ('name', 'description')  # 검색 기능
    ordering = ('-created_at',)  # 기본 정렬 기준

admin.site.register(Memo, MemoAdmin)