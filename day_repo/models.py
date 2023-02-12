# Create your models here.
from django.contrib.auth import get_user_model
from django.db import models

# ユーザモデルの取得
User = get_user_model()


# 日報モデル
class ReportModel(models.Model):
    class Meta:
        verbose_name = "日報"
        verbose_name_plural = "日報一覧"

    # ID(主キーは)自動生成のため割愛
    # 登録ユーザ(モデルと紐づけ)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # タイトル：100字以内
    title = models.CharField(verbose_name="タイトル", max_length=100)
    # 報告内容：1000字以内
    content = models.TextField(verbose_name="報告内容", max_length=1000)
    # 作成日時
    created_date_time = models.DateTimeField('作成日時', auto_now_add=True)

    # タイトル表示
    def __str__(self):
        return self.title


# 画像アップロード用モデル
class ImageUpload(models.Model):
    # タイトル(100字以内)
    title = models.CharField(max_length=100)
    # 画像データ
    img = models.ImageField(upload_to="images")

    # タイトル表示
    def __str__(self):
        return self.title
