from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db import models


# Userモデルのモデルマネージャー
class UserManager(BaseUserManager):

    # 一般ユーザ作成
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # スタッフユーザ作成
    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    # 管理者ユーザ作成
    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


# 自作Userモデル
class User(AbstractBaseUser):
    # 管理画面表示用設定
    class Meta:
        verbose_name = "ユーザ"
        verbose_name_plural = "ユーザ一覧"

    # メールアドレス
    email = models.EmailField(
        verbose_name='Eメールアドレス',
        max_length=255,
        unique=True,
    )
    # 有効化済み
    active = models.BooleanField(default=True)
    # スタッフフラグ
    staff = models.BooleanField(default=False)
    # 管理者フラグ
    admin = models.BooleanField(default=False)

    # メールアドレスのキー化
    USERNAME_FIELD = 'email'

    objects = UserManager()

    # コンストラクタ
    def __str__(self):
        return self.email

    # パーミッション確認
    def has_perm(self, perm, obj=None):
        return self.admin

    # パーミッション確認(モジュール)
    def has_module_perms(self, app_label):
        return self.admin

    # スタッフ確認
    @property
    def is_staff(self):
        return self.staff

    # 管理者確認
    @property
    def is_admin(self):
        return self.admin

    # 有効化チェック
    @property
    def is_active(self):
        return self.active


# ユーザモデルの拡張項目
class Profile(models.Model):
    # 紐づけ元Userモデル
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # ユーザ名
    username = models.CharField(max_length=100, verbose_name="ユーザー名")
    # 部署名
    department = models.CharField(max_length=100, blank=True, null=True, verbose_name="部署")
    # 電話番号
    phone_number = models.IntegerField(blank=True, null=True, verbose_name="携帯番号")
    # 性別
    gender = models.CharField(max_length=1, default=None, verbose_name="性別", blank=True, null=True, choices=[
        (None, "--"),
        ("m", "男性"),
        ("f", "女性")
    ])
    # 誕生日
    birthday = models.DateField(blank=True, null=True, verbose_name="生年月日")

    # コンストラクタ
    def __str__(self):
        return self.username
