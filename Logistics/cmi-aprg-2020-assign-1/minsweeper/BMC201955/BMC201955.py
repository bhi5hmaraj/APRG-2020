import sys
lst = list(map(int,input().split(" ")))
m = lst[0]
n = lst[1]
matrix = []
for i in range(m):
    matrix.append(list(input()))

def func(i,j,list1):
    l = 0
    m1 = len(list1)
    n1 = len(list1[0])
    m2 = (i-1)
    n2 = (j-1)
    m3 = (i+2)
    n3 = (j+2)
    for p in range(m2,m3):
        for q in range(n2,n3):
            if (p in range(m1)) and (q in range(n1)) and ((p != i) or (q != j)) and (list1[p][q] == '*'):
                l = l+1      
    return(l)

outd = ""
for i1 in range(m):
    for j1 in range(n):
      if matrix[i1][j1] != '*':
        outd = outd + str(func(i1,j1,matrix))
      else:
        outd = outd + matrix[i1][j1]
    outd = outd + "\n"
            
sys.stdout.write(outd)
