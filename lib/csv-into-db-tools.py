def replace_col_csv(fileLoc: str, toReplace: str, newReplace: str):
    line_content = []
    # Lendo o .csv:
    with open(file=fileLoc, mode='r', encoding='utf-8') as fp:
        line = fp.readline()

        while line:
            line_replaced = line.replace(f',', ' ')
            line_replaced = line_replaced.replace(f'"', '')
            line_content.append(line_replaced.strip())
            line = fp.readline()
        
    with open(file=fileLoc, mode='w', encoding='utf-8') as fp:
        for line in line_content:
            fp.write(line + '\n')