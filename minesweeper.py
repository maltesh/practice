import sys

filename = sys.argv[1]

fp = open(filename, 'r')
lines = fp.readlines()
index = 0
for line in iter(lines):
    matrix=[]
    if len(line.rstrip('\n').split(' ')) == 2:
        size = line.rstrip('\n').split(' ')
        rows = size[0]
        columns = size[1]

        # print rows,columns
        if rows == 0 == columns:
            sys.exit(1)
        for ii in range(int(rows)):
            matrix.append(list(lines[1 + index].rstrip('\n')))
            index = index + 1
        index=index+1

        temp = [[0 for j in range(int(columns))] for i in range(int(rows))]
        for item in enumerate(matrix):
            idx = item[0]
            row = item[1]
            for col in enumerate(row):
                col_idx = col[0]
                col_item = col[1]
                if col_item == '*':
                    valid_columns = [i for i in [col_idx + 1, col_idx - 1, col_idx] if i >= 0 and i < len(row)]
                    valid_rows = [i for i in [idx + 1, idx - 1, idx] if i >= 0 and i <len(matrix)]
                    for k in valid_rows:
                        for i in valid_columns:
                            if matrix[k][i] != '*':
                                temp[k][i] = temp[k][i] + 1


        print temp

# import sys
#
# __name__ = "Minesweeper safety algorithm"
# __author__ = "Naren Aryan"
# __date__ = "10-01-2015 11:00PM"
#
# with open(sys.argv[1]) as f:
#     # Break Input into lines;
#     lines = f.readlines()
#     counter,field_count = 0,0
#     # Process Fields in the Input. When you see a 0,0 field then Exit.
#
#     while int(lines[counter].split()[0]) != 0:
#         field_count += 1
#         init_line = lines[counter].split()
#         counter += 1
#         # import ipdb;ipdb.set_trace()
#         process_matrix = []
#         for i in range(int(init_line[0])):
#             process_matrix.append([lines[counter][j] for j in range(int(init_line[1]))])
#
#             counter += 1
#         # Copy original matrix to modifying matrix
#         print process_matrix
#         backup_matrix = process_matrix
#         for row_index, row in enumerate(process_matrix):
#             for col_index, col in enumerate(row):
#                 # When you encounter a '.' then check six cell wheel for mines.
#
#                 if col == '.':
#                     valid_rows = [i for i in [row_index + 1, row_index - 1, row_index] if i >=0 and i<len(process_matrix)]
#
#                     valid_columns = [i for i in [col_index + 1, col_index - 1, col_index] if i >=0 and i<len(row)]
#                     print row_index,'---',col_index
#                     print valid_rows," -->\n"
#                     print valid_columns,"===>\n"
#
#
#                     print [process_matrix[mini_row][mini_col] for mini_row in valid_rows for mini_col in valid_columns]
#                     # count total mines linear, diagonal and update backup_matrix
#                     backup_matrix[row_index][col_index] = [process_matrix[mini_row][mini_col] for mini_row in valid_rows for mini_col in valid_columns].count('*')
#         print("\nField %d" % field_count)
#         for row_element in backup_matrix:
#             print(''.join([str(i) for i in row_element]))
