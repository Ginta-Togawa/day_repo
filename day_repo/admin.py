from django.contrib import admin

from day_repo.models import ReportModel

# Register your models here.

# 管理画面に日報モデルを表示
admin.site.register(ReportModel)
