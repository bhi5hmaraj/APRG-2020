n = int(input())
child,fam = [],[]
for i in range(n):
    child.append([])
    fam.append(-99)
for i in range(n-1):
    u,v = map(int,input().split())
    fam[v-1] = u
    child[u-1].append(v)
root = -1
for i in range(n):
    if(fam[i] == -99):
        root = i
root+=1
li = [0 for i in range(n)]                                  
query = []
for j in range(n):
    if child[j] == [] :
        query.append(j+1)

while(query != []):
    new_q = query.pop(0)
    if(child[new_q-1] == []):
        li[new_q-1] = 1
    else:
        c1, c2 = 0, 1
        for elem in child[new_q-1]:
            c1 += li[elem-1]
            if(child[elem-1] != []):
                for i in child[elem-1]:
                    c2 += li[i-1]
        li[new_q-1] = max(c2, c1)
    if(fam[new_q-1] != -99):
        query.append(fam[new_q-1])
print(li[root-1])
