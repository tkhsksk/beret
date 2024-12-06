from django.db import models

# Create your models here.
class User(models.Model):
    name       = models.CharField(max_length=255, verbose_name="ユーザー名")
    first_name = models.CharField(max_length=50, null=True, verbose_name="氏名1")
    last_name  = models.CharField(max_length=50, null=True, verbose_name="氏名2")
    password   = models.CharField(max_length=255, verbose_name="パスワード")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "フロントユーザー"

class UserImages(models.Model):
    user       = models.ForeignKey(User, on_delete=models.PROTECT)
    image      = models.ImageField(max_length=255, blank=True, null=True, upload_to='image/user', verbose_name="ユーザー画像")
    status     = models.CharField(max_length=1, default='E', verbose_name="有効状態")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "ユーザー画像"
