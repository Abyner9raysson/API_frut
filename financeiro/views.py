import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Financeiro

@csrf_exempt
def financeiro_view(request):
    if request.method == 'GET':
        financeiro = Financeiro.objects.all().values()
        return JsonResponse(list(financeiro), safe=False)
    
    elif request.method == 'POST':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        compra = data.get('compra')
        venda = data.get('venda')
        fiscal = data.get('fiscal')
        relatorio_compra = data.get('relatorioCompra')
        relatorio_venda = data.get('relatorioVenda')
        
        if not all([compra, venda, fiscal, relatorio_compra, relatorio_venda]):
            return JsonResponse({'message': 'Campos inválidos, preencha todos os campos'}, status=400)
        if Financeiro.objects.filter(compra=compra).exists():
            return JsonResponse({'message': 'financeiro já cadastrado'},status=409)
        
        financeiro = Financeiro(compra=compra, venda=venda, fiscal=fiscal, relatorioCompra=relatorio_compra, relatorioVenda=relatorio_venda)
        financeiro.save()
        
        return JsonResponse({'message': 'Registro financeiro adicionado com sucesso'}, status=200)
    

    elif request.method == 'PUT':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        compra = data.get('compra')
        venda = data.get('venda')
        fiscal = data.get('fiscal')
        relatorio_compra = data.get('relatorioCompra')
        relatorio_venda = data.get('relatorioVenda')
        
        if not all([compra, venda, fiscal, relatorio_compra, relatorio_venda]):
            return JsonResponse({'message': 'Campo inválido, preencha o campo fiscal'}, status=400)
        
        try:
            financeiro = Financeiro.objects.get(fiscal=fiscal)
        except Financeiro.DoesNotExist:
            return JsonResponse({'message': 'Registro financeiro não encontrado'}, status=404)
        
        financeiro.compra = compra
        financeiro.venda = venda
        financeiro.fiscal = fiscal
        financeiro.relatorioCompra = relatorio_compra
        financeiro.relatorioVenda = relatorio_venda
        financeiro.save()
        
        return JsonResponse({'message': 'Registro financeiro atualizado com sucesso'}, status=200)
    



    elif request.method == 'DELETE':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        fiscal = data.get('fiscal')
        
        if not fiscal:
            return JsonResponse({'message': 'Campo inválido, forneça o fiscal'}, status=400)
        
        try:
            financeiro = Financeiro.objects.filter(fiscal=fiscal).first()
        except Financeiro.DoesNotExist:
            return JsonResponse({'message': 'Registro financeiro não encontrado'}, status=404)
        
        financeiro.delete()
        
        return JsonResponse({'message': 'Registro financeiro excluído com sucesso'}, status=200)
    
    else:
        return JsonResponse({'message': 'Método inválido'}, status=405)
