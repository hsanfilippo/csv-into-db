import psycopg2
from psql_tables import *

colunas_tabela = ['nome', 'cpf', 'idade', 'telefone']
tipos_coluna = ['VARCHAR(30)', 'VARCHAR(11)', 'INTEGER', 'INTEGER']
types_list = [123, None, True, 'John', 1.23]
conv_type_list = conv_types(typesList=types_list)

try:
    connect = psycopg2.connect(
        user='postgres',
        password='your_pass_1337',
        host='127.0.0.1',
        port='5432',
        database='your_db'
    )

    cursor = connect.cursor()
    create_table_query = f"""{create(tableName='teste_create', colNames=colunas_tabela, colTypes=conv_type_list)}"""
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

