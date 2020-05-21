[row,col] = list(map(int,input().split()))
matrix = []
extra = []
for i in range(row):
    matrix.append(list('.'+input()+'.'))
for j in range(col+2): extra.append('.')
matrix = [extra]+matrix+[extra]
def adjacent_count(i,j):
    if (matrix[i][j] == '*'):return '*' 
    return ([matrix[i-1][j-1],matrix[i-1][j],matrix[i-1][j+1],matrix[i][j-1],matrix[i][j+1],matrix[i+1][j-1],matrix[i+1][j],matrix[i+1][j+1]].count('*'))
for i in range(1,row+1):
    for j in range(1,col+1): print(adjacent_count(i,j),end='')
    print()
