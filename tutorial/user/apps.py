from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tutorial.user' # tutorial 디렉토리 내의 user라는 도메인
    
