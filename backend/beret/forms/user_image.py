# フォームのクラスをインポート
from django import forms
# モデルをインポート
from beret.models import *
from beret.models import UserImages

# Musicialモデルを利用したMusicialFormを作成

class UserImageForm(forms.ModelForm):

    class Meta:
        # モデルはUserを使用
        model = UserImages
        # フィールドはすべてを利用
        fields = ["image"]
        ##  右のように個別指定してもOK → fields = ["name"]