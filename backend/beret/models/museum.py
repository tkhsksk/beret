from django.db import models
from beret.models import Manager

# Create your models here.
class Museum(models.Model):
    manager           = models.ForeignKey(Manager, on_delete=models.PROTECT, verbose_name="作成管理者id")
    name              = models.CharField(max_length=255, verbose_name="美術館名")
    mail              = models.EmailField(max_length=255, blank=True, null=True, verbose_name="メールアドレス")
    tel               = models.CharField(max_length=7, null=True, verbose_name="郵便番号")
    post              = models.PositiveIntegerField(verbose_name="郵便番号")
    address1          = models.CharField(max_length=152, verbose_name="住所1")
    address2          = models.CharField(max_length=152, verbose_name="住所2")
    profile           = models.TextField(max_length=5000, blank=True, null=True, verbose_name="プロフィール文")
    status            = models.BooleanField(default=False, verbose_name="ステータス")
    started_hour_at   = models.PositiveSmallIntegerField(verbose_name="開始時間")
    started_munute_at = models.PositiveSmallIntegerField(verbose_name="開始分")
    ended_hour_at     = models.PositiveSmallIntegerField(verbose_name="終了時間")
    ended_munute_at   = models.PositiveSmallIntegerField(verbose_name="終了分")
    latitude          = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name="緯度")
    longitude         = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True, verbose_name="経度")
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "美術館"
