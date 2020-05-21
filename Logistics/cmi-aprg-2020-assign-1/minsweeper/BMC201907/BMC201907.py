(m, n) = tuple(map(int, input().split()))
zeroes = [[0 for i in range(n)] for j in range(m)]

def tiles(m, n):
    matrix = []
    for i in range(m):
        matrix.append([x for x in input()])
    return (matrix)
solve = tiles(m, n)

for row in range(0, m):
    for col in range(0, n):
        if solve[row][col] == '*':
            zeroes[row][col] = '*'
        elif solve[row][col] == '.':
            for rowCheck in range(row - 1, row + 2):
                    for colCheck in range(col - 1, col + 2):
                        if (0 <= rowCheck < m) and (0 <= colCheck < n):
                            if solve[rowCheck][colCheck] == '*':
                                zeroes[row][col] += 1

for i in range(m):
    for x in zeroes[i]:
        print(x, end = '')
    print('')
    
