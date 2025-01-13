"""
URL configuration for tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from tutorial.user.views import UserViewSet
from tutorial.memo.views import MemoViewSet

urlpatterns = [
    path('admin/', admin.site.urls),

    # User
    path('users', UserViewSet.as_view({'post': 'create'}), name='user-register'),  # 회원가입
    path('users/login', UserViewSet.as_view({'post': 'login'}), name='user-login'),  # 로그인
    path('users/<int:pk>', UserViewSet.as_view({'get': 'retrieve'}), name='user-retrieve'),  # 사용자 조회
    # Memo
    path('memos', MemoViewSet.as_view({'post': "create", "get": "list"})),  # 메모 생성 / 조회
    path('memos/<int:pk>', MemoViewSet.as_view({"put": "update", "delete": "destroy"}))  # 메모 업데이트 / 삭제
]
