from django.shortcuts import render

import json
from django.http import JsonResponse

from .models import Usuarios

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def cad_view(request):
    if request.method == 'GET':
        usuarios = Usuarios.objects.all().values()
        return JsonResponse(list(usuarios), safe=False)
    
    elif request.method == 'POST':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        username = data.get('username')
        senha = data.get('senha')

        if not all([username, senha]):
            return JsonResponse({'message': 'Campos inválidos, preencha todos os campos'}, status=400)

        if Usuarios.objects.filter(username=username).exists():
            return JsonResponse({'message': 'Usuário existente'}, status=409)

        user = Usuarios(username=username, senha=senha)
        user.save()
        return JsonResponse({'status': 'cadastrado com sucesso'}, status=200)
    
    elif request.method == 'PUT':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        username = data.get('username')
        senha = data.get('senha')

        if not all([username, senha]):
            return JsonResponse({'message': 'Campos inválidos, preencha todos os campos'}, status=400)

        try:
            user = Usuarios.objects.get(username=username)
        except Usuarios.DoesNotExist:
            return JsonResponse({'message': 'Usuário não encontrado'}, status=404)

        user.senha = senha
        user.save()

        return JsonResponse({'status': 'Usuário atualizado com sucesso'}, status=200)
    
    elif request.method == 'DELETE':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        username = data.get('username')

        try:
            user = Usuarios.objects.get(username=username)
        except Usuarios.DoesNotExist:
            return JsonResponse({'message': 'Usuário não encontrado'}, status=404)

        user.delete()

        return JsonResponse({'status': 'Usuário excluído com sucesso'}, status=200)

    return JsonResponse({'message': 'Método inválido'}, status=405)