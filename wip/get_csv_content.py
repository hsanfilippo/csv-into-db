def get_csv_lines(file_loc: str) -> list:

    with open(file=file_loc, mode='r', encoding='utf-8') as fp:
        csv_lines = [] 
        line = fp.readline()
        line = fp.readline()

        while line:
            conv_list = []
            line_content = line.strip().split(sep=',')
            for content in line_content:
                content = content.replace("'", "")
                try:
                    if '.' in content:
                        content = float(content)
                    else:
                        content = int(content)
                except ValueError:
                    pass
                conv_list.append(content)
            csv_lines.append(conv_list)
            line = fp.readline()

    return csv_lines

print(get_csv_lines('./csv_lib/alimentos.csv'))