#FLood FIll Algorithm
#http://helvidios.blogspot.in/2011/12/10267-graphical-editor.html

import sys



filename = sys.argv[1]
lines = open(filename).readlines()
matrix = []
valid_commands = ['I', 'C', 'L', 'V', 'H', 'K', 'F', 'S', 'X']
row_size = 0
col_size = 0
for line in lines:
    cmd_line_args = line.rstrip("\n").split(' ')
    command = cmd_line_args[0]
    command_line_params = cmd_line_args[1:]
    if command in valid_commands:
        if command != 'X':
            if command == 'I':
                command_line_params = map(int, command_line_params)
                row_size = command_line_params[1]
                col_size = command_line_params[0]
                matrix = [[0 for i in range(command_line_params[0])] for j in range(command_line_params[1])]

            if command=='L':
                xrow = int(command_line_params[0])-1
                ycol = int(command_line_params[1])-1
                color = command_line_params[2]
                if xrow>=0 and ycol >=0 :
                    matrix[ycol][xrow]=color
            if command == 'V':
                col =  int(command_line_params[0])-1
                row1 = int(command_line_params[1])-1
                row2 = int(command_line_params[2])-1
                if row1>0 and row2>0 and col>0:
                    color = command_line_params[3]
                    while row1 <= row2:
                        matrix[row1][col]=color
                        row1=row1+1
            if command == 'H':
                col1 = int(command_line_params[0])-1
                col2 = int(command_line_params[1])-1
                row = int(command_line_params[2])-1
                color = command_line_params[3]
                while col1 <= col2:
                    matrix[row][col1]= color
                    col1=col1+1
            if command == 'S':
                file_name = command_line_params[0]
                fo = open("aa.txt", 'w')
                print matrix
                fo.write(str(matrix))
            if command == 'F':
                row = int(command_line_params[0])-1
                col = int (command_line_params[1])-1
                color = command_line_params[2]
                temp = matrix[:]
                # matrix[row][col]= color
                if row >= 0 and col >= 0 :
                    initial_color = temp[row][col]
                    i=0
                    for column_ele in enumerate(temp[row]):
                        print initial_color , temp[row],col , " ----> \n"
                        if column_ele[0] in [col, col + 1, col - 1]   and column_ele[1] == initial_color:
                            matrix[row][column_ele[0]]=color



        else:
            sys.exit(1)
