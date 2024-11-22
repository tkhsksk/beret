from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, verbose_name="ユーザー名")
    password = models.CharField(max_length=255, verbose_name="パスワード")

    class Meta:
        verbose_name_plural = "フロントユーザー"
