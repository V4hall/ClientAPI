# API Documentation - ClientAPI

## Clientes

### Cadastrar ou Consultar Clientes

**Endpoint:** `/clientes/`

**Métodos:**
- **GET**: Consulta clientes existentes. Pode ser filtrado por CPF ou Nome usando os parâmetros `cpf` ou `nome`.
- **POST**: Cadastra um novo cliente com endereços associados.

**Exemplo de consulta com filtro por CPF:**
`GET /clientes/?cpf=12345678900`


**Exemplo de consulta com filtro por Nome:**
`GET /clientes/?nome=João`


**Exemplo de requisição para cadastro de cliente:**
`POST /clientes/`
```json

{
    "nome_completo": "João da Silva",
    "cpf": "123.456.789-00",
    "telefone": "(11) 9876-5432",
    "email": "joao@example.com",
    "sexo": "M",
    "enderecos": [
        {
            "cep": "12345-678",
            "estado": "SP",
            "cidade": "São Paulo",
            "bairro": "Centro",
            "logradouro": "Rua Principal",
            "numero": "123"
        }
    ]
}
```


### Consultar, Atualizar ou Deletar um Cliente
**Endpoint:** `/clientes/<int:cliente_id>/`

**Métodos:**

- **GET**: Consulta detalhes de um cliente específico.
- **PUT**: Atualiza os dados de um cliente existente.
- **DELETE**: Deleta um cliente existente.


### Consultar ou Cadastrar Endereços para um Cliente
**Endpoint**: `/clientes/<int:cliente_id>/enderecos/`

**Métodos:**

- **GET**: Consulta os endereços associados a um cliente específico.
- **POST**: Cadastra endereços para um cliente existente.

**Exemplo de requisição para cadastro de endereços:**
`POST /clientes/<cliente_id>/enderecos/`

```json
[
    {
        "cep": "12345-678",
        "estado": "SP",
        "cidade": "São Paulo",
        "bairro": "Centro",
        "logradouro": "Rua Principal",
        "numero": "123"
    },
    {
        "cep": "12345-678",
        "estado": "RJ",
        "cidade": "Rio de Janeiro",
        "bairro": "Centro",
        "logradouro": "Avenida Central",
        "numero": "456"
    }
]
```

## Endereços

### Consultar, Atualizar ou Deletar um Endereço
**Endpoint**: `/enderecos/<int:endereco_id>/`

**Métodos:**

- **GET**: Consulta detalhes de um endereço específico.
- **PUT**: Atualiza os dados de um endereço existente.
- **DELETE**: Deleta um endereço existente.

## Estrutura de Dados

### Modelo de Dados - Endereco

```json
{
    "cep": "12345-678",
    "estado": "SP",
    "cidade": "São Paulo",
    "bairro": "Centro",
    "logradouro": "Rua Principal",
    "numero": "123"
}
```
### Modelo de Dados - Cliente
```json
{
    "nome_completo": "João da Silva",
    "cpf": "123.456.789-00",
    "telefone": "(11) 9876-5432",
    "email": "joao@example.com",
    "sexo": "M",
    "enderecos": [
        {
            "cep": "12345-678",
            "estado": "SP",
            "cidade": "São Paulo",
            "bairro": "Centro",
            "logradouro": "Rua Principal",
            "numero": "123"
        }
    ]
}
```

### Notas

- O campo `sexo` em Cliente aceita os valores `"M"` (Masculino), `"F"` (Feminino) ou `"O"` (Outro).
- O campo `enderecos` em Cliente aceita uma lista de objetos no formato de `Endereco`.
- Favor verificar se os requests possuem `/` no final.

### Endpoints

- `/clientes/`: Realiza consultas e cadastros de clientes.
- `/clientes/<cliente_id>/`: Realiza consultas, atualizações e exclusões de um cliente específico.
- `/clientes/<cliente_id>/enderecos/`: Realiza consultas e cadastros de endereços associados a um cliente.
- `/enderecos/<endereco_id>/`: Realiza consultas, atualizações e exclusões de um endereço específico.

