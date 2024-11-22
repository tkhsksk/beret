from django.shortcuts import render, redirect # redirectを追記
from beret.forms import UserForm # UserFormをimport
from beret.models import User

def index(request):

    users = User.objects.all()

    # HTMLで読み込むformを定義
    context = {
        'users': users,
    }
    return render(request, "home/index.html", context)
