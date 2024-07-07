def listar_tipos(lista: list):
    lista_com_os_tipos = []
    
    for item in lista:
        lista_com_os_tipos.append(type(item).__name__)
        
    for i, tipo in enumerate(lista_com_os_tipos):
        if tipo == 'float':
            lista_com_os_tipos[i] = 'DECIMAL(10,2)'
        elif tipo == 'str':
            lista_com_os_tipos[i] = 'TEXT'

    return lista_com_os_tipos