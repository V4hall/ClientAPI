from rest_framework import serializers

from .models import Cliente, Endereco


class EnderecoSerializer(serializers.ModelSerializer):
    """Serializador modelo Endereco."""
    class Meta:
        model = Endereco
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    """Serializador modelo Cliente."""
    enderecos = EnderecoSerializer(many=True, required=False)

    class Meta:
        model = Cliente
        exclude = ('id_endereco',)  # Exclui id_endereco do Response
        # fields = '__all__'

    def create(self, validated_data):
        """Criação de um novo cliente com endereços associados."""
        enderecos_data = validated_data.pop('enderecos', [])
        cliente = Cliente.objects.create(**validated_data)

        id_enderecos = []
        for endereco_data in enderecos_data:
            endereco, _ = Endereco.objects.get_or_create(**endereco_data)
            cliente.enderecos.add(endereco)
            id_enderecos.append(endereco.id)

        return cliente
