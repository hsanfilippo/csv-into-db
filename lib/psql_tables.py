def create(tableName: str, colNames: list, colTypes: list) -> str: 

    try:
        query_parts = list()
        query_content = str()
        
        for col_name, col_type in zip(colNames, colTypes):
            query_parts.append(f"{col_name} {col_type}")
            query_content = ", ".join(query_parts)
            final_query = f"""CREATE TABLE {tableName} ({query_content});"""

    except Exception as exc:
        print(f"{exc}")
    
    return final_query