from django.shortcuts import render, redirect # redirectを追記
from beret.forms import UserForm # UserFormをimport
from beret.forms import UserImageForm 
from beret.models import User
from beret.models import UserImages
from django.http import JsonResponse

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
    try:
        userImage = UserImages.objects.get(user_id=pk)
    except UserImages.DoesNotExist:
        userImage = None

    if request.method == "POST":
        # postデータを取得
        form = UserForm(request.POST, instance=user)
        formImage = UserImageForm(request.POST, request.FILES, instance=userImage)
    else:
        # フォームにデータを格納
        form = UserForm(instance=user)
        formImage = UserImageForm(instance=userImage)

    # htmlで読み込むformを定義
    context = {
        "form" : form,
        "user" : user,
        "image": userImage,
        "formImage": formImage,
    }

    if request.method == "POST":
        if 'confirm' in request.POST:
            return render(request, 'user/confirm.html', context)
        if 'editImage' in request.POST:
            newImage = formImage.save(commit=False)
            newImage.user = User.objects.get(id=pk)
            newImage.save()

            return redirect('user_edit', pk)
        if form.is_valid():
            form.save()
            return redirect('user_index')

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

def hoge(request):
    data = {}
    data['pinoko'] = 'アッチョンブリケ'
    form = UserImageForm()
    if request.method == "POST":
        form = UserImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False

    return JsonResponse(data)
