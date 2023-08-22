from django.db import models


class Endereco(models.Model):
    cep = models.CharField(max_length=10)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.logradouro}, {self.numero}"


class Cliente(models.Model):
    nome_completo = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    ativo = models.BooleanField(default=True)
    id_endereco = models.JSONField(blank=True, default=list)
    enderecos = models.ManyToManyField(Endereco, related_name='clientes')

    def __str__(self):
        return self.nome_completo


class ClienteEndereco(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='enderecos_associados', on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, related_name='clientes_associados', on_delete=models.CASCADE)

    def __str__(self):
        return f"Cliente: {self.cliente.nome_completo} - Endereço: {self.endereco.logradouro}, {self.endereco.numero}"
