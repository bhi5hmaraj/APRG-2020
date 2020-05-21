import sys
sys.setrecursionlimit(10**6)
l = list(map(int, input().split()))
matrix = []
for i in range (l[0]):
    matrix.append(list(input()))
def count(li,p):
    if li == []:
        return 0
    if p == li[0]:
        return count(li[1:],p) + 1
    else:
        return count (li[1:],p)
def realList(t,x,y,m,n):
    k1 = []
    k2 = []
    k3 = []
    k4 = []
    k5 = []
    k6 = []
    k7 = []
    k8 = []
    k = []
    if x > 0:
        k1 = [(t[x-1])[y]]
    else:
        k1 = k1
    if y > 0:
        k2 = [(t[x])[y-1]]
    else:
        k2 = k2
    if x > 0 and y > 0:
        k3 = [(t[x-1])[y-1]]
    else:
        k3 = k3
    if x < m - 1:
        k4 = [(t[x+1])[y]]
    else:
        k4 = k4
    if y < n - 1:
        k5 = [(t[x])[y+1]]
    else:
        k5 = k5
    if x < m - 1 and y > 0:
        k6 = [(t[x+1])[y-1]]
    else:
        k6 = k6
    if x < m - 1 and y < n - 1:
        k7 = [(t[x+1])[y+1]]
    else:
        k7 = k7
    if x > 0 and y < n - 1:
        k8 = [(t[x-1])[y+1]]
    k = k1 + k2 + k3 + k4 + k5 + k6 + k7 + k8
    return k
for i in range (l[0]):
    for j in range (l[1]):
        if (matrix[i])[j] == '*':
            (matrix[i])[j] = (matrix[i])[j]
        else:
            (matrix[i])[j] = count(realList(matrix,i,j,l[0],l[1]),'*')         
for i in range (l[0]):
    for x in matrix[i]:
        print(x,end='')
    print('')

        

        
    
    
