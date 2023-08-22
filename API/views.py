import re

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cliente, Endereco
from .serializers import ClienteSerializer, EnderecoSerializer


# View para cadastrar e consultar clientes
@api_view(['POST', 'GET'])
def cadastrar_consultar_clientes(request):
    if request.method == 'GET':
        # Obter parâmetros de pesquisa (CPF ou Nome)
        cpf = request.GET.get('cpf')
        nome = request.GET.get('nome')

        if cpf:
            # Filtro por CPF usando regex para deixar apenas números
            cpf = re.sub(r'\D', '', cpf)
            clientes = Cliente.objects.filter(cpf__icontains=cpf)
        elif nome:
            # Filtro por Nome
            clientes = Cliente.objects.filter(nome_completo__icontains=nome)
        else:
            # Listar todos os clientes
            clientes = Cliente.objects.all()

        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Cadastrar um novo cliente com endereços
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            enderecos_data = request.data.get('enderecos', [])
            cliente = serializer.save()

            id_enderecos = []
            for endereco_data in enderecos_data:
                endereco, _ = Endereco.objects.get_or_create(**endereco_data)
                cliente.enderecos.add(endereco)
                id_enderecos.append(endereco.id)

            cliente.id_endereco = id_enderecos
            cliente.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View para consultar/atualizar/deletar um cliente específico
@api_view(['GET', 'PUT', 'DELETE'])
def consultar_atualizar_cliente(request, cliente_id):
    try:
        cliente = Cliente.objects.get(pk=cliente_id)
    except Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data="Cliente deletado com sucesso!")


# View para consultar os endereços de um cliente (GET) ou Cadastrar enderecos a um cliente (POST)
@api_view(['GET', 'POST'])
def consultar_cadastrar_enderecos(request, cliente_id):
    try:
        cliente = Cliente.objects.get(pk=cliente_id)

        if request.method == 'GET':
            enderecos = cliente.enderecos.all()
            serializer = EnderecoSerializer(enderecos, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            enderecos_data = request.data
            enderecos_ids = cliente.id_endereco  # Obtém a lista atual de IDs de endereços

            for endereco_data in enderecos_data:
                serializer = EnderecoSerializer(data=endereco_data)
                if serializer.is_valid():
                    endereco = serializer.save()
                    cliente.enderecos.add(endereco)
                    enderecos_ids.append(endereco.id)  # Adiciona o novo ID à lista
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # Atualiza o campo id_endereco do cliente com a lista acumulativa de IDs de endereços
            cliente.id_endereco = enderecos_ids
            cliente.save()

            return Response({"message": "Endereços cadastrados com sucesso."}, status=status.HTTP_201_CREATED)

    except Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data="Não foi possível encontrar o cliente ou o endereço")


# View para consultar/atualizar/deletar um endereço específico
@api_view(['GET', 'PUT', 'DELETE'])
def consultar_atualizar_endereco(request, endereco_id):
    try:
        endereco = Endereco.objects.get(pk=endereco_id)
    except Endereco.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EnderecoSerializer(endereco)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EnderecoSerializer(endereco, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        cliente = endereco.clientes.first()  # Busque o cliente relacionado ao endereço
        cliente.id_endereco.remove(endereco.id)  # Remove o ID do endereço da lista
        cliente.enderecos.remove(endereco)  # Remove o endereço do cliente
        cliente.save()  # Salva as alterações no cliente
        endereco.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data="Endereço deletado com sucesso!")
