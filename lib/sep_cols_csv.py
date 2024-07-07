def sep_cols_csv(file_loc: str):

    # Lendo o .csv:
    with open(file=file_loc, mode='r', encoding='utf-8') as fp:
        fp.readline()
        line = fp.readline()

        # Aqui irá o tratamento necessário dos dados contidos no .csv.
        # Para tratar os dados, estou desenvolvendo alguns métodos, para que sejam importados sempre que necessários.

        while line:
            line_element = line.split(sep=',')
            line_alim['nome'] = line_element[0]
            line_alim['kcal_g'] = float(line_element[1])
            line_alim['prot_g'] = float(line_element[2])
            line_alim['carb_g'] = float(line_element[3])
            line_alim['gord_g'] = float(line_element[4])

            alim_list.append(line_alim)
            line = fp.readline()



sep_cols_csv('./csv_lib/alimentos.csv')
