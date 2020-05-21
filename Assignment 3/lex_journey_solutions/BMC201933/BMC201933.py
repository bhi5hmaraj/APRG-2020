li1 = list(map(int, input().split()))
n = li1[0]
m = li1[1]
li2 = list(map(int, input().split()))
p = li2[0]
q = li2[1]
G = [[] for i in range(n)]
        
        
for i in range(m):
    li = list(input().split())
    G[int(li[0]) - 1 ].append((int(li[2])-1,li[1]))
    G[int(li[2]) -1].append((int(li[0])-1,li[1]))
def sp(A,x,y):
    x = x - 1
    y = y - 1
    
    mark = [0 for i in range(n)]
    distance = [-2020 for i in range(n)]
    parent = [[]  for i in range(n)]
    req    = [0 for i in range(n)]
    q = []
    mark[x] = 1
    distance[x] = 0
    req = ['' for x in range(n)]
    q.append(x)
    while (q != [] and mark[y] != 1):
        v = q[0]
        for i in A[v]:
            if mark[i[0]] == 0:
                mark[i[0]] = 1
                q.append(i[0])
                distance[i[0]]= distance[v] + 1
                li = ''
                for x in  A[i[0]]:
                    if distance[x[0]] == distance[v] and ((req[x[0]] + x[1]) < li or li == ''):
                        li = req[x[0]] + x[1]
                req[i[0]] = li
        q.pop(0)
        req[v] = ''
    return req[y]
    if q == []:
        return 0
    else:
        l = distance[y]
        umark = [-2020 for i in range(n)]
        w = []
        w.append(y)
        umark[y] = l
        count = 1
        while (w != []):
            v = w[0]
            for i in A[v]:
                if  mark[i[0]] == 1 and distance[i[0]] == (distance[v] - 1) and umark[i[0]] == -2020:
                        umark[i[0]] = distance[i[0]]
                        w.append(i[0])
                        count = count + 1
            w.pop(0)
        journey = ['',[x]]     
        index = l 
        while index > 0:
            k = len(journey[1])
            for i in range(k):
                v = journey[1][i]
                li = ['',[]]
                for x in  A[v]:
                    if umark[x[0]] == (l - index + 1) and (x[1]<li[0] or li[0] == ''):
                        li = [x[1],[x[0]]]
                
                    elif umark[x[0]] == (l - index  + 1) and x[1]  == li[0]:
                        li[1].append(x[0])
                journey[1][i] = li
            li = journey[1][0]
            for i in range(k):
                if journey[1][i][0] < li[0]:
                    li = journey[1][i]
                if journey[1][i][0] == li[0]:
                    li[1] = li[1] + journey[1][i][1]
            journey[0] = journey[0] + li[0]
            journey[1] = li[1]
            index = index - 1
        return journey[0]
                           
print(sp(G,p,q))                  
            