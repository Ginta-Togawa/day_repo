from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


# 管理画面上のユーザモデル設定
class UserAdmin(BaseUserAdmin):
    # 一覧表示
    list_display = (
        "email",
        "active",
        "staff",
        "admin",
    )

    # 絞り込み
    list_filter = (
        "admin",
        "active",
    )
    # ソート
    ordering = ("email",)
    # 検索対象フィールド
    search_fields = ('email',)
    # 項目のカスタマイズ(なし)
    filter_horizontal = ()

    # ユーザ追加時の入力項目
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )

    # ユーザ更新時の入力項目
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('staff', 'admin',)}),
    )


# 管理画面に自作ユーザモデルを表示
admin.site.register(User, UserAdmin)
