import uuid
import os.path

from django.db import models
from beret.models import User
from beret.models import Event

def get_image_path(self, filename):
    prefix = 'image/user/'
    name = str(uuid.uuid4()).replace('-', '')
    extension = os.path.splitext(filename)[-1]
    return prefix + name + extension

# Create your models here.
class Review(models.Model):
    user       = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="ユーザーid")
    event      = models.ForeignKey(Event, on_delete=models.PROTECT, verbose_name="イベントid")
    rate       = models.PositiveSmallIntegerField(verbose_name="評価")
    title      = models.CharField(max_length=255, verbose_name="タイトル")
    notes      = models.TextField(max_length=5000, blank=True, null=True, verbose_name="レビュー文")
    status     = models.CharField(max_length=1, default='D', verbose_name="ステータス")
    visited_at = models.DateField(blank=True, null=True, verbose_name="訪問日")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "レビュー"

class ReviewImage(models.Model):
    event      = models.ForeignKey(Event, on_delete=models.PROTECT, verbose_name="イベントid")
    review     = models.ForeignKey(Review, on_delete=models.PROTECT, verbose_name="レビューid")
    title      = models.CharField(max_length=255, blank=True, null=True, verbose_name="タイトル")
    status     = models.CharField(max_length=1, default='E', verbose_name="ステータス")
    image      = models.ImageField(max_length=255, blank=True, null=True, upload_to=get_image_path, verbose_name="画像path")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "レビュー画像"
