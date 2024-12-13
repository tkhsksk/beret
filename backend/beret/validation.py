import re
import uuid
import os.path

from django.core.exceptions import ValidationError

def check_post(value):
    if len(value) != 7:
        raise ValidationError('郵便番号は7桁で入力してください')
    if not value.isdecimal():
        raise ValidationError('郵便番号は数字のみで構成してください')

def check_password(value):
    REX = r"(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,255}"
    result = re.fullmatch(REX, value)
    if not result:
        raise ValidationError("右記のパスワード条件に従って入力してください")

def get_image_path(self, filename):
    prefix = 'image/user/'
    name = str(uuid.uuid4()).replace('-', '')
    extension = os.path.splitext(filename)[-1]
    return prefix + name + extension