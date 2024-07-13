# READ AND CONVERT PYTHON TYPES INTO POSTGRESQL TYPES:
def conv_types(typesList: list):
    final_types = []

    for item in typesList:
        final_types.append(type(item).__name__)
        
    for i, typ in enumerate(final_types):
        if typ == 'float':
            final_types[i] = 'DECIMAL(10,2)'
        elif typ == 'str':
            final_types[i] = 'TEXT'
        elif typ == 'int':
            final_types[i] = 'INTEGER'
        elif typ == 'bool':
            final_types[i] = 'BOOLEAN'

    return final_types

# CREATES A BRAND NEW DB BASED ON A CSV FILE:
def create(tableName: str, colNames: list, colTypes: list) -> str: 
    try:
        query_parts = list()
        query_content = str()
        
        for col_name, col_type in zip(colNames, conv_types(colTypes)): # CALLS CONV_TYPES()
            query_parts.append(f"{col_name} {col_type}")
            query_content = ", ".join(query_parts)
            final_query = f"""CREATE TABLE {tableName} ({query_content});"""

    except Exception as exc:
        print(f"{exc}")
    
    return final_query

# INSERTS DATA INTO A DB BASED ON A CSV FILE:
def insert(tableName: str, cols: list, values: list) -> str:
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