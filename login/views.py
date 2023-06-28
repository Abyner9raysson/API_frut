from django.shortcuts import render
import json
from django.http import JsonResponse
from cadastro.models import Usuarios
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        username=data.get('username')
        senha=data.get('senha')
        if not all ([username,senha]):
            return JsonResponse({'message':'preencha os campos'})
        if Usuarios.objects.filter(username=username,senha=senha).exists():
            return JsonResponse({'message': 'Login efetuado com SUCESSO!'},status=200)
        else:
            return JsonResponse({'message': 'Login e/ou senha incorretos'},status=400)
    return JsonResponse({'message': 'Metodo inválido'}, status=405)