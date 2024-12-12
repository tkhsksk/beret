import secrets
import string

from django.http import JsonResponse

def password(request, pk):

    data = {}
    pass_chars = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(pass_chars) for x in range(pk))

    if request.method == "GET":
        data['res'] = True
        data['passwd'] = password

    return JsonResponse(data)
