# フォームのクラスをインポート
from django import forms
# モデルをインポート
from .models import *
INPUT_CLASSES = 'text-black placeholder-gray-600 w-full px-4 py-2.5 mt-2 text-base transition duration-500 ease-in-out transform border-transparent rounded-lg bg-gray-200 focus:border-cyan-500 focus:bg-white dark:focus:bg-gray-800 focus:outline-none focus:shadow-outline focus:ring-2 ring-offset-current ring-offset-2 ring-gray-400'

# Musicialモデルを利用したMusicialFormを作成
class UserForm(forms.ModelForm):
    #image = forms.ImageField(widget=forms.FileInput)
    class Meta:
        # モデルはUserを使用
        model = User
        # フィールドはすべてを利用
        fields = (
            'name',
            'first_name',
            'last_name',
            'image',
            'password',
        )
        ##  右のように個別指定してもOK → fields = ["name"]
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'first_name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'last_name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'password': forms.TextInput(attrs={'class': INPUT_CLASSES}),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['image'].required = False