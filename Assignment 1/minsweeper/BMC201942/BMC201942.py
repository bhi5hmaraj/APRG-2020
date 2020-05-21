def mine_number(field, i, j):
    k = 0
    m, n = field_dim(field)
    for a in range(-1,2):
        if (i+a) in range(0, m):
            for b in range(-1,2):
                if (j+b) in range(0, n):
                    if field[i+a][j+b] == "*":
                       k+=1
    return k

def field_dim(field):
    return len(field), len(field[1])

def solution(field):
    sol = []
    m, n = field_dim(field)
    for i in range(0,m):
        sol.append("")
        for j in range(0,n):
            if field[i][j] == "*":
                sol[i] = sol[i] + "*"
            else:
                sol[i] = sol[i] + str((mine_number(field, i, j)))
    return sol

field = []
m, n = input().split()
m, n = int(m), int(n)
for i in range(0, m):
    val = input()
    field.append(val)
for str in solution(field):
    print(str)

