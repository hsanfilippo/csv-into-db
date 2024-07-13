def sep_cols_csv(file_loc: str):

    # Lendo o .csv:
    with open(file=file_loc, mode='r', encoding='utf-8') as fp:
        header_list = [] # Container dos titulos das colunas

        line = fp.readline()
        line_content = line.split(sep=',')
        for item in line_content:
            header_list.append(item.strip())
        line = fp.readline()

        while line:
            line_alim = {} # Declarando o dict que sera usado no for abaixo
            line_content = line.split(sep=',')

            for hdr_i, line_c in zip(header_list, line_content):
                line_alim[hdr_i] = line_c.strip()

        # Ajustando os tipos para se adequar a tabela no PostgreSQL:



            print(line_alim[hdr_i])
            line = fp.readline()




        # print(header_list)


        # fp.readline() # Apenas le a linha ate o final, e pula para a proxima

        # Aqui irá o tratamento necessário dos dados contidos no .csv.
        # Para tratar os dados, estou desenvolvendo alguns métodos, para que sejam importados sempre que necessários.

            # line_alim['nome'] = line_element[0]
            # line_alim['kcal_g'] = float(line_element[1])
            # line_alim['prot_g'] = float(line_element[2])
            # line_alim['carb_g'] = float(line_element[3])
            # line_alim['gord_g'] = float(line_element[4])




sep_cols_csv('../csv_lib/alimentos.csv')
