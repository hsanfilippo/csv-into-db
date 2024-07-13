# INSERTS DATA INTO A DB BASED ON A CSV FILE:
def insert_psql(tableName: str, cols: list, values: list) -> str:
    try:
        query_temp = list()
        query_col = str()
        query_val = str()
        
        for col_name in cols:
            query_temp.append(f"{col_name}")
            query_col = ", ".join(query_temp)

        query_temp = []

        for value in values:
            if type(value).__name__ == 'str':
                query_temp.append(f"'{value}'")
            else:
                query_temp.append(f"{value}")
            
            query_val = ", ".join(query_temp)

        final_query = f"""INSERT INTO {tableName} ({query_col}) VALUES ({query_val});"""

    except Exception as exc:
        print(f"{exc}")
    
    return final_query