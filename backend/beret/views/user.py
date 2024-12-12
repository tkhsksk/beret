from django.shortcuts import render, redirect # redirectを追記
from beret.forms import UserForm # UserFormをimport
from beret.forms import UserImageForm 
from beret.models import User
from beret.models import UserImages

def index(request):
    users = User.objects.order_by('-id')
    latest = User.objects.order_by('-created_at').first()
    # userImages = UserImages.objects.all()
    if 'res' in request.session:
        request.session.clear()

    # HTMLで読み込むformを定義
    context = {
        'users': users,
        'choices': UserForm.STATUS_CHOICES,
        'latest': latest,
        # 'user_images': userImages,
    }
    return render(request, "user/index.html", context)

def create(request):
    # フォームを作成
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)

    # HTMLで読み込むformを定義
    context = {
        'form': form,
        "choices": form.STATUS_CHOICES,
    }

    # メソッドがPOSTだった場合
    if request.method == "POST":
        # POSTデータを取得
        if 'confirm' in request.POST:
            if form.is_valid():
                return render(request, 'user/confirm.html', context)

        # データが有効か確認
        if form.is_valid():
            # user = form.save()
            # user.set_password(user.password)
            # user.save()
            form.save()
            return redirect('user_index')

    return render(request, "user/create.html", context)

def edit(request, pk):
    # Userモデルからidを元にデータを取得
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        # 存在しなければリダイレクト
        return redirect('user_index')

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
        "choices": form.STATUS_CHOICES,
    }

    if request.method == "POST":
        if 'confirm' in request.POST:
            if form.is_valid():
                return render(request, 'user/confirm.html', context)
            else:
                render(request, "user/edit.html", context)
        if form.is_valid():
            form.save()
            # request.session['res'] = 'success'
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

def upload_image(request):
    from django.http import JsonResponse

    data = {}
    data['method'] = request.method
    data['post'] = request.POST

    if request.method == "POST":
        try:
            userImage = UserImages.objects.get(user_id=request.POST['user_id'])
        except UserImages.DoesNotExist:
            userImage = None
        form = UserImageForm(request.POST, request.FILES, instance=userImage)
        data['errors'] = form.errors
        data['valid'] = form.is_valid()

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user_id = request.POST['user_id']
            obj.save()
            return JsonResponse(data)

    return JsonResponse(data)
