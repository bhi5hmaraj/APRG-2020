def final_ans(Graph, _s, _d): 
    row = len(Graph) 
    col = len(Graph[0]) 
    leng = [float("Inf")] * row 
    visited =[0] * row 
    pathlength =[0] * row 
    parent = [-1] * row 
    leng[_s]= 0
    for count in range(row-1): 
        u = min_leng(leng, visited)
        if u == float("Inf"): 
            break
        else:
            visited[u]= 1 
        for v in range(row): 
            if visited[v]== 0 and Graph[u][v] and leng[u]+Graph[u][v]<leng[v]: 
                parent[v]= u 
                pathlength[v]= pathlength[parent[v]]+1
                leng[v]= leng[u]+Graph[u][v] 
            elif visited[v]== 0 and Graph[u][v] and leng[u]+Graph[u][v]== leng[v] and pathlength[u]+1<pathlength[v]: 
                parent[v]= u 
                pathlength[v] = pathlength[u] + 1
    if leng[_d]!= float("Inf"):
        return (PrintPath(parent, _d)) 
    else: 
        return []

ans = []

def PrintPath(parent, _d): 
    if parent[_d]==-1: 
        ans.append(_d)
        return
    PrintPath(parent, parent[_d]) 
    ans.append (_d)
    return ans

def min_leng(leng, visited): 
    min = float("Inf") 
    for v in range(len(leng)): 
        if not visited[v] and leng[v]<min: 
            min = leng[v] 
            Min_index = v 
    return float("Inf") if min == float("Inf") else Min_index 

n, m = map(int, input().split())
l_cost = list(map(int, input().split()))
dict1 = {}
inp = []
vals = []
for i in range(n):
    inp1 = list(map(int, input().split()))
    inp.append(inp1)
    vals = vals + inp1
    w = l_cost[i]

A = [[0]*(max(vals) + 1) for _ in range(max(vals) + 1)]    
for i in range(n):    
    inp1 = inp[i]
    w = l_cost[i]
    for j in range(len(inp1) - 1):
        u, v = inp1[j], inp1[j+1]
        if (u, v) not in dict1:
            dict1.update({(u, v): w})
        elif (u, v) in dict1:
            w2 = dict1[(u, v)]
            if w < w2:
                dict1.update({(u, v): w})
        if A[u][v] > l_cost[i] and A[u][v] != 0:
            A[u][v] = (l_cost[i]) * (max(u, v) - min(u, v))
        elif A[u][v] == 0:
            A[u][v] = (l_cost[i])  * (max(u, v) - min(u, v))
        if A[v][u] > l_cost[i] and A[v][u] != 0:
            A[v][u] = (l_cost[i]) * (max(u, v) - min(u, v))
        elif A[v][u] == 0:
            A[v][u] = (l_cost[i]) * (max(u, v) - min(u, v))
g = (A)
abc = final_ans(g, 0, m)
#print(dict1)
pri = 0
trans = []
for i in range(len(ans) - 1):
    pri+=(A[(ans[i])][(ans[i+1])])
    if (ans[i], ans[i+1]) in dict1:
        trans.append(dict1[(ans[i], ans[i+1])])
    elif (ans[i], ans[i+1]) not in dict1:
        trans.append(dict1[(ans[i+1], ans[i])])
#trans = list(set(trans))

if 0 not in vals or m not in vals:
    print('IMPOSSIBLE')
elif ans == []:
    print('IMPOSSIBLE')
elif vals.count(0) == vals.count(m) == 1:
    ind = 0
    in1 = 0
    for j in inp:
        if m in j and 0 in j:
            ind = inp.index(j)
            in1+=1
            break
    if in1 == 1:
        print(m*(l_cost[ind]))
    else:
        factor = 0
        current = trans[0]
        for i in range(1, len(trans)):
            if trans[i] != current:
                factor+=1
                current = trans[i]
        #print(factor)
        print(str(pri + (60 * (factor))))
else:
    factor = 0
    current = trans[0]
    for i in range(1, len(trans)):
        if trans[i] != current:
            factor+=1
            current = trans[i]
    #print(factor)
    print(str(pri + (60 * (factor))))
