def get_csv_lines(file_loc: str) -> list:

    with open(file=file_loc, mode='r', encoding='utf-8') as fp:
        csv_lines = [] 
        line = fp.readline()
        line = fp.readline()

        while line:
            line_content = line.split(sep=',')
            line_content[-1] = line_content[-1].strip()
            csv_lines.append(line_content)
            line = fp.readline()

    return csv_lines

print(get_csv_lines('./csv_lib/alimentos.csv'))
