types_list = [123, None, True, 'John', 1.23]

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

    return final_types

print(conv_types(typesList=types_list))