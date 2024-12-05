from django.db import models

# Create your models here.
class User(models.Model):
    name       = models.CharField(max_length=255, verbose_name="ユーザー名")
    first_name = models.CharField(max_length=50, null=True, verbose_name="氏名1")
    last_name  = models.CharField(max_length=50, null=True, verbose_name="氏名2")
    image      = models.ImageField(max_length=255, blank=True, null=True, upload_to='image/user', verbose_name="ユーザー画像")
    password   = models.CharField(max_length=255, verbose_name="パスワード")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "フロントユーザー"
