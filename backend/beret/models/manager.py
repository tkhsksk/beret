from django.db import models

# Create your models here.
class Manager(models.Model):
    name       = models.CharField(max_length=255, verbose_name="マネージャー名")
    first_name = models.CharField(max_length=50, null=True, verbose_name="氏名1")
    last_name  = models.CharField(max_length=50, null=True, verbose_name="氏名2")
    password   = models.CharField(max_length=255, verbose_name="パスワード")
    mail       = models.EmailField(max_length=255, unique=True, verbose_name="メールアドレス")
    profile    = models.TextField(max_length=5000, blank=True, null=True, verbose_name="プロフィール文")
    status     = models.BooleanField(default=False, verbose_name="ステータス")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "管理者"
