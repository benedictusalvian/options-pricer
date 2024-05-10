from ANSI import BLUE, COLOR_END

def print_tables(data):

    # Print headers
    headers = data[0].pop(0)[0], data[1].pop(0)[0], data[2].pop(0)[0], data[3].pop(0)[0]
    headers = [element.ljust(32) if element != headers[0] else element.ljust(33) for element in headers]
    print("".join(headers))
    
    # Print rest of table
    max_rows = max(len(table) for table in data)
    num_tables = len(data)

    # Fill missing rows with empty strings
    for table in data:
        while len(table) < max_rows:
            table.append([''] * len(table[0]))

    # Print tables side by side
    for row in range(max_rows):
        for table in range(num_tables):
            for col in range(len(data[table][0])):
                if row == 11:
                    print(BLUE + str(data[table][row][col]) + COLOR_END, end='\t')
                else:
                    print(data[table][row][col], end='\t')
            print('\t', end=' ')
        print()

