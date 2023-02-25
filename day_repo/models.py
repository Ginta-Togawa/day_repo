# Create your models here.
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q

from day_repo.utils.random_string import random_string_generator

# ユーザモデルの取得
User = get_user_model()


# 日報検索用QuerySetクラス
class ReportModelQuerySet(models.QuerySet):

    # 検索処理
    def search(self, query=None):
        qs = self
        # 公開フラグでフィルター
        qs = qs.filter(release_flag=True)
        if query is not None:
            or_lookup = (Q(title__icontains=query) | Q(content__icontains=query))
            qs = qs.filter(or_lookup).distinct()
        # 作成日時の降順
        return qs.order_by("-created_date_time")


# 日報モデル用マネージャークラス
class ReportModelManager(models.Manager):
    # 一覧取得
    def get_queryset(self):
        return ReportModelQuerySet(self.model, using=self._db)

    # 検索
    def search(self, query=None):
        return self.get_queryset().search(query=query)


# 日報モデルのslugデフォルト値設定
def slug_maker():
    repeat = True
    while repeat:
        new_slug = random_string_generator()
        counter = ReportModel.objects.filter(slug=new_slug).count()
        if counter == 0:
            repeat = False
    return new_slug


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
    # 公開フラグ
    release_flag = models.BooleanField(verbose_name="公開する", default=False)
    # スラッグ
    slug = models.SlugField(max_length=20, unique=True, default=slug_maker)

    objects = ReportModelManager()

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
