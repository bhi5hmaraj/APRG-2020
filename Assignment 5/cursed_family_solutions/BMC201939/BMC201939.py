#Largest independent set of a tree
n = int(input())
parent = [None for i in range(n)]
children = [[] for i in range(n)]

for i in range(n-1):
    I = list(map(int,input().split()))
    parent[I[1]-1] = I[0]
    children[I[0]-1].append(I[1])
    
for i in range(n):
    if(parent[i] == None):
        root = i+1
A = [0 for i in range(n)]                                  #A[i] stores answer for subtree rooted at Node[i+1]
Q = [(j+1) for j in range(n) if children[j] == []]

while(Q):
    z = Q.pop(0)
    if(children[z-1] == []):
        A[z-1] = 1
    else:
        A_exc = 0
        A_inc = 1
        for elem in children[z-1]:
            A_exc += A[elem-1]
            if(children[elem-1] != []):
                for g in children[elem-1]:
                    A_inc += A[g-1]
        A[z-1] = max(A_inc, A_exc)
    if(parent[z-1] != None):
        Q.append(parent[z-1])
     

    
    
    
#print(A)
print(A[root-1])