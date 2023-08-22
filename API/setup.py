import os
import sys
import mysql.connector
from django.core.management import execute_from_command_line

# Obter o diretório atual do script
script_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.abspath(os.path.join(script_directory, ".."))
sys.path.append(project_directory)


def setup_database_and_tables():
    """
    Configuração automatizada do banco de dados e tabelas para a aplicação ClientAPI.

    Esta função realiza as seguintes etapas:
    1. Conecta-se ao banco de dados MySQL (localhost).
    2. Cria um banco de dados "ClientAPI", se ainda não existir.
    3. Fecha a conexão temporariamente.
    4. Gera migrações e aplica as migrações para criar as tabelas.
    5. Inicializa o servidor Django para a aplicação.

    Nota: Esta função é mais adequada para ambientes de desenvolvimento ou configurações iniciais,
    e não deve ser utilizada em ambientes de produção sem as devidas precauções.

    """
    try:
        # Conexao com banco
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root123'
        )

        # Cria um banco de dados (caso ele não exista)
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ClientAPI")

        print("Configuração do banco de dados concluída com sucesso.")

        # Fecha conexao
        cursor.close()
        connection.close()

        # Criar as tabelas
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ClientAPI.settings")
        execute_from_command_line(["manage.py", "makemigrations"])
        execute_from_command_line(["manage.py", "migrate"])

        print("Tabelas criadas com sucesso.")

        # Rodar o servidor Django
        execute_from_command_line(["manage.py", "runserver"])

    except mysql.connector.Error as err:
        print('Não foi possível configurar o banco.')
        print(f"Error: {err}")


if __name__ == "__main__":
    setup_database_and_tables()
