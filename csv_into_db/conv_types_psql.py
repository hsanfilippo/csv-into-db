# READ AND CONVERT PYTHON TYPES ON A LIST INTO POSTGRESQL TYPES:
def conv_types_psql(typesList: list):
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