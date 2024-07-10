import psycopg2
from psql_tables import *

colunas_tabela = ['nome', 'cpf', 'idade', 'telefone']
tipos_coluna = ['VARCHAR(30)', 'VARCHAR(11)', 'INTEGER', 'INTEGER']

try:
    connect = psycopg2.connect(
        user='postgres',
        password='your_pass_1337',
        host='127.0.0.1',
        port='5432',
        database='your_db'
    )

    cursor = connect.cursor()
    create_table_query = f"""{create(tableName='teste_create', colNames=colunas_tabela, colTypes=tipos_coluna)}"""
    cursor.execute(create_table_query)
    connect.commit()

    print("Tabela criada com sucesso!")

except Exception as error:
    print(f"Ocorreu um erro: {error}")

finally:
    if cursor is not None:
        cursor.close()
    if connect is not None:
        connect.close()

