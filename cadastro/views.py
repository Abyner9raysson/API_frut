from django.shortcuts import render

import json
from django.http import JsonResponse

from .models import Usuarios

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def cad_view(request):
    if request.method == 'POST':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        username=data.get('username')
        senha=data.get('senha')
        if not all ([username,senha]):
            return JsonResponse({'message':'campos inválidos, preencha-o'},status=400)
        if Usuarios.objects.filter(username=username).exists():
            return JsonResponse({'message': 'Usuário Existente'},status=409)
        
        user= Usuarios(username=username,senha=senha)
        user.save()
        return JsonResponse({'status': 'Usuario já cadastrado'}, status=200)
    return JsonResponse({'message': 'Metodo inválido'}, status=405)