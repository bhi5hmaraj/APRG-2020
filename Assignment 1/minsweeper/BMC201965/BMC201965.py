from functools import *

l = list(map(int,input().split()))
r = l[0]
c = l[1]

field = []
for i in range(r):
    field.append(list(map(lambda x:x if x == "*" else "0",list(input()))))

for i in range(r):
    for j in range(c):
        if field[i][j] == "*":
            for x in [k for k in [i-1,i,i+1] if k>=0]:
                for y in [l for l in [j-1,j,j+1] if l>=0]:
                    try:
                        field[x][y] = str(1+int(field[x][y]))
                    except:
                        pass

field1 = list(map(lambda x:reduce(lambda y,z:y+z,x,""),field))
list(map(print,field1))
