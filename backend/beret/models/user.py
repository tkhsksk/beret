import uuid
import os.path

from django.db import models

def get_image_path(self, filename):
    prefix = 'image/user/'
    name = str(uuid.uuid4()).replace('-', '')
    extension = os.path.splitext(filename)[-1]
    return prefix + name + extension

# Create your models here.
class User(models.Model):
    name       = models.CharField(max_length=255, verbose_name="ユーザー名")
    first_name = models.CharField(max_length=50, null=True, verbose_name="氏名1")
    last_name  = models.CharField(max_length=50, null=True, verbose_name="氏名2")
    password   = models.CharField(max_length=255, verbose_name="パスワード")
    mail       = models.EmailField(max_length=255, unique=True, default='', verbose_name="メールアドレス")
    post       = models.PositiveIntegerField(null=True, verbose_name="郵便番号")
    address1   = models.CharField(max_length=152, null=True, verbose_name="住所1")
    address2   = models.CharField(max_length=152, null=True, verbose_name="住所2")
    profile    = models.TextField(max_length=5000, null=True, verbose_name="プロフィール文")
    notes      = models.TextField(max_length=5000, null=True, verbose_name="管理側ノート")
    status     = models.CharField(max_length=1, default='E', verbose_name="ステータス")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "フロントユーザー"
# INSERT beret_userimages (id,image,status,user_id,created_at,updated_at) VALUES (1,'702a05f3131249f3bbcfe65d25afafc7.jpg','E',1,'2020-01-01 00:00:00','2020-01-01 00:00:00');
class UserImages(models.Model):
    user       = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="ユーザーid")
    image      = models.ImageField(max_length=255, blank=True, null=True, upload_to=get_image_path, verbose_name="ユーザー画像")
    status     = models.CharField(max_length=1, default='E', verbose_name="ステータス")
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
