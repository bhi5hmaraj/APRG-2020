n = int(input())

inList = [[] for _ in range(n+1)]
outList = [[] for _ in range(n+1)]

for i in range(n-1):
    p,s = map(int, input().split())
    inList[s].append(p)
    outList[p].append(s)

def Root(inList):
    for i in range(1,n+1):
        if len(inList[i])==0:
            return i

AnsList = [[-1,-1] for _ in range(n+1)]

def find_max(v,bool):
    if bool == True :
        if AnsList[v][1] == -1:
            son_sum = 0
            for u in outList[v]:
                son_sum += find_max(u,False)
            AnsList[v][1] = 1 + son_sum
        return AnsList[v][1]
    else:
        if AnsList[v][0] == -1:
            son_sum = 0
            for u in outList[v]:
                son_sum += max(find_max(u,False),find_max(u,True))
            AnsList[v][0] = son_sum
        return AnsList[v][0]

root = Root(inList)

print(max(find_max(root,False),find_max(root,True)))