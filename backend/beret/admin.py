from django.contrib import admin
from .models import User # Userモデルをimport

# Register your models here.

admin.site.register(User) # Userモデルを使えるようにする