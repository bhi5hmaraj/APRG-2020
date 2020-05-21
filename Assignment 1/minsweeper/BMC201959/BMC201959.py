input_list = [int(x) for x in input().split()]
row_numbers = input_list[0]
column_numbers = input_list[1]
matrix = [['.']* (column_numbers + 2)]
list1 = []
for i in range(row_numbers):
    matrix.append(['.'] + list(input()) + ['.'])
matrix.append(['.']* (column_numbers + 2))
for x in range(1,row_numbers + 1):
    for y in range(1,column_numbers + 1):
        if matrix[x][y] == '*':
            matrix[x][y] = matrix[x][y]
        else:
            list1 = [matrix[x][y+1],matrix[x][y-1],matrix[x-1][y],matrix[x-1][y-1],matrix[x-1][y+1],matrix[x+1][y],matrix[x+1][y-1],matrix[x+1][y+1]]
            matrix[x][y] = str(list1.count('*'))
matrix = list(map(lambda t:t[1:-1],matrix))[1:-1]
for a in range(row_numbers):
    print(''.join(matrix[a]))
