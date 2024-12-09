from django.db import models
from beret.models import Museum
from beret.models import Manager

# Create your models here.
class Event(models.Model):
    museum     = models.ForeignKey(Museum, on_delete=models.PROTECT, verbose_name="美術館id")
    manager    = models.ForeignKey(Manager, on_delete=models.PROTECT, verbose_name="作成管理者id")
    rate       = models.DecimalField(max_digits=11, decimal_places=10, null=True, verbose_name="評価")
    title      = models.CharField(max_length=255, verbose_name="タイトル")
    notes      = models.TextField(max_length=5000, blank=True, null=True, verbose_name="紹介文")
    mail       = models.EmailField(max_length=255, blank=True, null=True, verbose_name="メールアドレス")
    tel        = models.IntegerField(blank=True, null=True, verbose_name="電話番号")
    url        = models.URLField(max_length=255, blank=True, null=True, verbose_name="イベントページ")
    status     = models.CharField(max_length=1, default='E', verbose_name="ステータス")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "イベント"
