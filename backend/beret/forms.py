# フォームのクラスをインポート
from django import forms
# モデルをインポート
from .models import User

# Musicialモデルを利用したMusicialFormを作成
class UserForm(forms.ModelForm):
    class Meta:
        # モデルはUserを使用
        model = User
        # フィールドはすべてを利用
        fields = '__all__'
        ##  右のように個別指定してもOK → fields = ["name"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
            'password': forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
        }