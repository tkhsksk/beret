from django.core.validators import *
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from beret.validation import *

# 拡張ユーザーモデル用のマネージャー
class UserManager(UserManager):

    # 通常・管理者ユーザー共通の登録
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('メールアドレスは必須です')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 通常ユーザーの設定
    def manage_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_manager', False)
        extra_fields.setdefault('is_admin', False)
        return self.create_user(email, password, **extra_fields)

    # 管理者ユーザーの設定
    def manage_adminuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_manager', True)
        extra_fields.setdefault('is_admin', True)
        if extra_fields.get('is_manager') is not True:
            raise ValueError('管理者ユーザーはis_managerがTrueの必要があります')
        if extra_fields.get('is_admin') is not True:
            raise ValueError('管理者ユーザーはis_adminがTrueの必要があります')
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username   = models.CharField(max_length=255, unique=True, verbose_name="ユーザー名", validators=[MinLengthValidator(3), MaxLengthValidator(14)])
    first_name = models.CharField(max_length=50, null=True, verbose_name="氏名1", validators=[MinLengthValidator(1), MaxLengthValidator(50)])
    last_name  = models.CharField(max_length=50, null=True, verbose_name="氏名2", validators=[MinLengthValidator(1), MaxLengthValidator(50)])
    password   = models.CharField(max_length=255, verbose_name="パスワード", validators=[check_password])
    mail       = models.EmailField(max_length=255, unique=True, default='', verbose_name="メールアドレス")
    post       = models.CharField(max_length=7, null=True, verbose_name="郵便番号", validators=[check_post])
    address1   = models.CharField(max_length=152, null=True, verbose_name="住所1", validators=[MaxLengthValidator(152)])
    address2   = models.CharField(max_length=152, null=True, verbose_name="住所2", validators=[MaxLengthValidator(152)])
    profile    = models.TextField(max_length=5000, null=True, verbose_name="プロフィール文", validators=[MaxLengthValidator(5000)])
    notes      = models.TextField(max_length=5000, null=True, verbose_name="管理側ノート", validators=[MaxLengthValidator(5000)])
    status     = models.BooleanField(default=False, verbose_name="ステータス")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "フロントユーザー"

# INSERT beret_userimages (id,image,status,user_id,created_at,updated_at) VALUES (1,'702a05f3131249f3bbcfe65d25afafc7.jpg','E',1,'2020-01-01 00:00:00','2020-01-01 00:00:00');
# select group_concat(table_name) from information_schema.tables where table_schema = 'beret' and table_name regexp 'beret_.*' \G

class UserImages(models.Model):
    user       = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="ユーザーid")
    image      = models.ImageField(max_length=255, blank=True, null=True, upload_to=get_image_path, validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'webp'])], verbose_name="ユーザー画像")
    status     = models.BooleanField(default=True, verbose_name="ステータス")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "ユーザー画像"

class UserCredit(models.Model):
    user         = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="ユーザーid")
    payment_code = models.CharField(max_length=255, verbose_name="決済idhash")
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "ユーザーカード情報"
