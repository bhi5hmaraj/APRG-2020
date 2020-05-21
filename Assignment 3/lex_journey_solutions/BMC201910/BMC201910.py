def BFS(anfang, kurz):
    queue = []
    queue.append(anfang)
    #kurz is like short
    
    kurz[anfang] =0
    while queue:
        #spass is the template
        
        spass = queue.pop(0)
        for i in range(len(AJ[spass])):
            j = AJ[spass][i][0]
            if kurz[j] ==-1:
                kurz[j] = kurz[spass]+1
                queue.append(j)


def finden():
    if x ==y:
        return ""
    s = ""
    nodes =[x]
    nodes_ =[]
    while len(nodes)!= 0:
        cha = None
        flag = 0
        for i in nodes:
            if cha== None or cha> mins[i]:
                cha = mins[i]
        
        s =s+cha 
        for i in range(len(nodes)):
            if mins[nodes[i]] ==cha:
                for j in range(len(AJ[nodes[i]])): 
                    nd = nodes[i]
                    val = AJ[nd][j][0]
                    char = AJ[nd][j][1]
                    if val==y:
                        flag =1
                        break
                    if kurz_x[nd]+1+kurz_y[val] == kurz_x[y] and char == cha and visited[val] == 0:
                        visited[val] =1
                        nodes_.append(val)
        if flag ==1:
            break
        nodes = nodes_
        nodes_ =[]

    return(s)
#ill take input



l1=list(map(int,input().split()))
n=l1[0]
m=l1[1]


l2=list(map(int,input().split()))
x=l2[0]
y=l2[1]

kurz_x =[(-1) for i in range(n+1)]
kurz_y =[(-1) for i in range(n+1)]
mins = [None for i in range(n+1)]
visited = [0  for i in range(n+1)]
AJ  = [[] for i in range(n+1)]



#changing adj

for i in range(m):
    s = str(input()).split()
    u = int(s[0])
    v = int(s[2])
    c = s[1]
    AJ[u].append([v,c])
    AJ[v].append([u,c])



BFS(x, kurz_x)
BFS(y, kurz_y)

for i in range(1,n+1):
    if kurz_x[i] + kurz_y[i] == kurz_x[y]:
        spass = None 
        for j in range(len(AJ[i])):
            val = AJ[i][j][0]
            char = AJ[i][j][1]
            if kurz_x[i] + 1 + kurz_y[val] == kurz_x[y]:
                if spass == None:
                    spass = char 
                elif char < spass:
                    spass = char 
                else:
                    continue
        mins[i] = spass 

print(finden())