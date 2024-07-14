def get_csv_header(file_loc: str) -> list:

    with open(file=file_loc, mode='r', encoding='utf-8') as fp:
        header_list = [] 

        line = fp.readline()
        line_content = line.split(sep=',')
        for item in line_content:
            header_list.append(item.strip())

    return header_list

print(get_csv_header('./csv_lib/alimentos.csv'))
