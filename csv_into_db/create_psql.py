# CREATES A BRAND NEW DB BASED ON A CSV FILE:
def create_psql(tableName: str, colNames: list, colTypes: list) -> str: 
    import conv_types_psql

    query_parts = list()
    query_content = str()
    final_query = str()

    try:
        for col_name, col_type in zip(colNames, conv_types_psql.conv_types_psql(colTypes)):
            query_parts.append(f"{col_name} {col_type}")
            query_content = ", ".join(query_parts)
            final_query = f"""CREATE TABLE {tableName} ({query_content});"""
        
    except Exception as exc:
        print(f"{exc}")
    
    return final_query

colunas_nome = ['nome', 'telefone', 'cidade']
colunas_tipo = ['str', 'str', 'str']