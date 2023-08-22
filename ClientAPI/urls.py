"""
ClientAPI URL Configuration
"""
from django.urls import path
from API.views import *

urlpatterns = [
    # Cadastrar um cliente com endereços (POST)
    # ou Consulta Cliente (GET)
    # Pode ser usado com filtros, como ?cpf= ou ?nome=
    path('clientes/', cadastrar_consultar_clientes, name='cadastrar-consultar-clientes'),

    # Consultar detalhes de um cliente específico (GET)
    # ou Atualizar dados de um cliente existente (PUT)
    # ou Deletar um cliente existente (DELETE)
    path('clientes/<int:cliente_id>/', consultar_atualizar_cliente, name='consultar-atualizar-cliente'),

    # Consultar os endereços de um cliente específico (GET)
    # ou Cadastrar enderecos a um cliente existente. (POST)
    path('clientes/<int:cliente_id>/enderecos/', consultar_cadastrar_enderecos, name='consultar-cadastrar-enderecos'),

    # Atualizar dados de um endereço existente (PUT)
    # ou Consultar um endereço existente (GET)
    # ou Deletar um endereço existente (DELETE)
    path('enderecos/<int:endereco_id>/', consultar_atualizar_endereco, name='consultar-atualizar-endereco'),
]
