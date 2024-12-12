# フォームのクラスをインポート
from django import forms
# モデルをインポート
from beret.models import *
from django.core.exceptions import ValidationError

INPUT_CLASSES = 'text-black placeholder-gray-400 w-full px-4 py-2.5 mt-2 text-base transition duration-500 ease-in-out transform border-transparent rounded-lg bg-gray-200 focus:border-cyan-500 focus:bg-white dark:focus:bg-gray-800 focus:outline-none focus:shadow-outline focus:ring-2 ring-offset-current ring-offset-2 ring-gray-400'

# Musicialモデルを利用したMusicialFormを作成
class UserForm(forms.ModelForm):
    STATUS_CHOICES = (
        (True, '有効' ,'rose'),
        (False, '無効' ,'neutral'),
    )

    class Meta:
        # モデルはUserを使用
        model = User
        # フィールドはすべてを利用
        fields = (
            'name',
            'first_name',
            'last_name',
            'mail',
            'post',
            'address1',
            'address2',
            'profile',
            'notes',
            'password',
            'status',
        )
        ##  右のように個別指定してもOK → fields = ["name"]
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder':'例）ユーザ名'}),
            'first_name': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder':'例）ベレ田'}),
            'last_name': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder':'例）太郎'}),
            'mail': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'post': forms.TextInput(attrs={'class': INPUT_CLASSES+' w-[10rem]', 'size':7, 'placeholder':'例）1510053'}),
            'address1': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder':'例）東京都練馬区'}),
            'address2': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'profile': forms.Textarea(attrs={'class': INPUT_CLASSES, 'placeholder':'ユーザーはプロフィールを登録していません'}),
            'notes': forms.Textarea(attrs={'class': INPUT_CLASSES, 'placeholder':'管理者はノートを登録していません'}),
            'password': forms.TextInput(attrs={'class': INPUT_CLASSES}),
        }

    status = forms.BooleanField(
        label='有効状態',
        widget=forms.CheckboxInput(attrs={'class': 'sr-only peer hidden'}),
    )

    def clean(self):
        cleaned_data = super().clean()
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']

        if first_name:
            if not last_name:
                raise ValidationError('* 名字を入力する場合は名前も入力してください', code="error0001")
        if last_name:
            if not first_name:
                raise ValidationError('* 名前を入力する場合は名字も入力してください', code="error0002")
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['post'].required = False
        self.fields['address1'].required = False
        self.fields['address2'].required = False
        self.fields['profile'].required = False
        self.fields['notes'].required = False
        self.fields['status'].required = False
