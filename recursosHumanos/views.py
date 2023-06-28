from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import RecursosH

@csrf_exempt
def RH_view(request):
    if request.method == 'GET':
        recurso = RecursosH.objects.all().values()
        return JsonResponse(list(recurso), safe=False)
   
    elif request.method == 'POST':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        nome = data.get('nome')
        cargo = data.get('cargo')
        salario = data.get('salario')
        cargaHoraria = data.get('carga_horaria')
        folhaPonto = data.get('folha_ponto')
        setor = data.get('setor')

        if not all([nome, cargo, salario, cargaHoraria, folhaPonto, setor]):
            return JsonResponse({'message': 'preencha todos os campos'}, status=400)

        if not RecursosH.objects.filter(nome=nome):
            recursos = RecursosH(nome=nome, cargo=cargo, salario=salario, cargaHoraria=cargaHoraria,folhaPonto=folhaPonto,setor=setor)
            recursos.save()
            return JsonResponse({'message': 'adicionado com sucesso'}, status=200)

        else:
            return JsonResponse({'message': 'Funcionario já existe'})
        

    if request.method == 'PUT':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        nome = data.get('nome')
        cargo = data.get('cargo')
        salario = data.get('salario')
        cargaHoraria = data.get('carga_horaria')
        folhaPonto = data.get('folha_ponto')
        setor = data.get('setor')

        if not all([nome, cargo, salario, cargaHoraria, folhaPonto, setor]):
            return JsonResponse({'message': 'preencha todos os campos'}, status=400)

        try:
            recursos = RecursosH.objects.get(nome=nome,cargo=cargo) #recebe o nome e cargo para poder atualizar
        except RecursosH.DoesNotExist:
            return JsonResponse({'message': 'Funcionario não encontrado'}, status=404)

        recursos.nome = nome
        recursos.cargo = cargo
        recursos.salario = salario
        recursos.cargaHoraria = cargaHoraria
        recursos.folhaPonto = folhaPonto
        recursos.setor = setor

        recursos.save()
        return JsonResponse({'message': 'Funcionario atualizado com sucesso'}, status=200)

    if request.method == 'DELETE':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        nome = data.get('nome')

        if not nome:
            return JsonResponse({'message': 'Campo inválido, forneça o nome'}, status=400)

        try:
            recursos = RecursosH.objects.get(nome=nome)
        except RecursosH.DoesNotExist:
            return JsonResponse({'message': 'Funcionario não encontrado'}, status=404)

        recursos.delete()
        return JsonResponse({'message': 'Funcionario excluído com sucesso'}, status=200)

    return JsonResponse({'message': 'Método inválido'}, status=405)