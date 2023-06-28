from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Estoque

@csrf_exempt
def estoque_view(request):
    if request.method == 'GET':
        estoque = Estoque.objects.all().values()
        return JsonResponse(list(estoque), safe=False)
    
    elif request.method == 'POST':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        setor = data.get('setor')
        corredor = data.get('corredor')
        prateleira = data.get('prateleira')
        produto = data.get('produto')
        
        if not all([setor, corredor, prateleira, produto]):
            return JsonResponse({'message': 'Campos inválidos, preencha todos os campos'}, status=400)
        
        if Estoque.objects.filter(produto=produto).exists():
            return JsonResponse({'message': 'Produto já existe'}, status=409)
        
        estoque = Estoque(setor=setor, corredor=corredor, prateleira=prateleira, produto=produto)
        estoque.save()
        return JsonResponse({'message': 'Produto adicionado com sucesso'}, status=200)

    elif request.method == 'PUT':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        produto = data.get('produto')
        
        if not produto:
            return JsonResponse({'message': 'Campo "produto" inválido'}, status=400)
        
        try:
            estoque = Estoque.objects.get(produto=produto)
        except Estoque.DoesNotExist:
            return JsonResponse({'message': 'Produto não encontrado'}, status=404)
        
        setor = data.get('setor')
        corredor = data.get('corredor')
        prateleira = data.get('prateleira')
        
        if not all([setor, corredor, prateleira]):
            return JsonResponse({'message': 'Campos inválidos, preencha todos os campos'}, status=400)
        
        estoque.setor = setor
        estoque.corredor = corredor
        estoque.prateleira = prateleira
        estoque.save()
        
        return JsonResponse({'message': 'Produto atualizado com sucesso'}, status=200)
    
    elif request.method == 'DELETE':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        produto = data.get('produto')
        
        if not produto:
            return JsonResponse({'message': 'Campo "produto" inválido'}, status=400)
        
        try:
            estoque = Estoque.objects.get(produto=produto)
        except Estoque.DoesNotExist:
            return JsonResponse({'message': 'Produto não encontrado'}, status=404)
        
        estoque.delete()
        return JsonResponse({'message': 'Produto excluído com sucesso'}, status=200)
    
    else:
        return JsonResponse({'message': 'Método inválido'}, status=405)
