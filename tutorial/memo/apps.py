# drf_tutorial/memo/apps.py
from django.apps import AppConfig


class MemoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tutorial.memo'
