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
    
    # print(line_content)

# replace_col_csv('./csv_lib/short_desc_col.csv')
