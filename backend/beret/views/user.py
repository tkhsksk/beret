from django.shortcuts import render, redirect # redirectを追記
from beret.forms import UserForm # UserFormをimport
from beret.models import User

def index(request):
    users = User.objects.all()

    # HTMLで読み込むformを定義
    context = {
        'users': users,
    }
    return render(request, "user/index.html", context)

def create(request):
    # フォームを作成
    form = UserForm()

    # メソッドがPOSTだった場合
    if request.method == "POST":
        # POSTデータを取得
        form = UserForm(request.POST)

        # データが有効か確認
        if form.is_valid():
            # 有効であればデータを格納
            form.save()
            # beret/urls.pyに設定したnameにリダイレクトする
            return redirect('user_index')

    # HTMLで読み込むformを定義
    context = {
        'form': form,
    }
    return render(request, "user/create.html", context)

def edit(request, pk):
    # Userモデルからidを元にデータを取得
    user = User.objects.get(id=pk)
    # フォームにデータを格納
    form = UserForm(instance=user)

    if request.method == "POST":
        # postデータを取得
        form = UserForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
            return redirect('user_index')

    # htmlで読み込むformを定義
    context = {
        "form": form,
        "user": user,
    }
    return render(request, "user/edit.html", context)

def search(request):
    query = request.GET.get('query')

    if query:
        users = User.objects.filter(
            name__icontains=query)
    else:
        users = User.objects.all()
    context = {"users": users}
    return render(request, "user/search.html", context)
