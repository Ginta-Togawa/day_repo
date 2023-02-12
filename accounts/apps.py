from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    # 管理画面表示用設定
    verbose_name = 'ユーザ管理'
