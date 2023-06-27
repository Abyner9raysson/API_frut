from django.shortcuts import render

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Produtos

# Create your views here.
@csrf_exempt
def produtos_view(request):
    if request.method == 'GET':
        produtos = Produtos.objects.all().values()
        return JsonResponse(list(produtos), safe=False)
    
    elif request.method == 'POST':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        quantidade = data.get('quantidade')
        descricao = data.get('descricao')
        nome = data.get('nome')
        preco = data.get('preco')
        categoria = data.get('categoria')
        tipo = data.get('tipo')
        
        if not all([quantidade, descricao, nome, preco, categoria, tipo]):
            return JsonResponse({'message': 'Campos inválidos, preencha todos os campos'}, status=400)
        if Produtos.objects.filter(nome=nome).exists():
            return JsonResponse({'message': 'Produto já cadastrado'},status=409)
        
        produto = Produtos(
            quantidade=quantidade,
            descricao=descricao,
            nome=nome,
            preco=preco,
            categoria=categoria,
            tipo=tipo
        )
        produto.save()
        return JsonResponse({'message': 'Produto adicionado com sucesso'}, status=200)
    
    elif request.method == 'PUT':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)

        novaQuantidade = data.get('quantidade')
        novaDescricao = data.get('descricao')
        nome = data.get('nome')
        novoPreco = data.get('preco')
        novaCategoria = data.get('categoria')
        novoTipo = data.get('tipo')

        if not all([novaCategoria, novaDescricao, novaQuantidade, novoPreco, novoTipo]):
             return JsonResponse({'message': 'Campos inválidos, preencha todos os campos'}, status=400)
        
        try:
            produto = Produtos.objects.get(nome=nome)
        except Produtos.DoesNotExist:
            return JsonResponse({'message': 'Produto não encontrado'}, status=404)
        
        produto.quantidade = novaQuantidade
        produto.descricao = novaDescricao
        produto.preco = novoPreco
        produto.categoria = novaCategoria
        produto.tipo = novoTipo
        
        produto.save()
        return JsonResponse({'message': 'Produto atualizado com sucesso'}, status=200)
    
    elif request.method == 'DELETE':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        nome = data.get('nome')
        
        try:
            produto = Produtos.objects.get(nome=nome)
        except Produtos.DoesNotExist:
            return JsonResponse({'message': 'Produto não encontrado'}, status=404)
        
        produto.delete()
        return JsonResponse({'message': 'Produto Excluido com sucesso'}, status=200)
    
    return JsonResponse({'message': 'Método inválido'}, status=405)