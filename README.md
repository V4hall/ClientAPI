# ClientAPI

A ClientAPI é uma API de gerenciamento de clientes e endereços construída com o Django Rest Framework. Ela permite que você gerencie eficientemente informações de clientes e seus endereços associados.

## Começando

Antes de executar o aplicativo, certifique-se de que as dependências sejam satisfeitas instalando os pacotes Python necessários executando o seguinte comando:

```bash
pip install -r requirements.txt
```

Após instalar as dependências, você precisa configurar o aplicativo executando o script `setup.py` localizado no diretório `/API/`:

```bash
python setup.py
```

Esse script realizará tarefas necessárias de configuração, como criar tabelas no banco de dados, aplicar migrações e configurar dados iniciais.

## Aviso
Este aplicativo foi desenvolvido apenas para fins de demonstração e teste. Não é recomendado o uso em produção devido a possíveis vulnerabilidades de segurança e falta de otimizações para ambientes de produção.

Além disso, este aplicativo está configurado com `DEBUG = True` no arquivo `settings.py`. 

## Uso
Após a conclusão de `setup.py` será automaticamente iniciada o servidor de desenvolvimento em `localhost`.
