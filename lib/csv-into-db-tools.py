def replace_col_csv(file_loc: str):

    line_content = []
    # Lendo o .csv:
    with open(file=file_loc, mode='r', encoding='utf-8') as fp:
        line = fp.readline()

        while line:
            line_replaced = line.replace(',', ' ')
            line_replaced = line_replaced.replace('"', '')
            line_content.append(line_replaced.strip())
            line = fp.readline()
        
    with open(file=file_loc, mode='w', encoding='utf-8') as fp:
        for line in line_content:
            fp.write(line + '\n')

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