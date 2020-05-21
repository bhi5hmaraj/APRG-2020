n = int(input())
relation = []
for i in range(n-1):
    relation.append(list(map(int, input().split())))
    
a = 0
reqanstable = [0 for i in range(n)]

Father = [None for i in range(n)]
Son_first = [set() for i in range(n)]
for i in relation:
    Father[i[1]-1] = i[0]-1
    Son_first[i[0]-1].add(i[1] - 1)
    
for i in range(n):
    if Father[i] is None:
        a = i
        break

    
grandchildren = [set() for i in range(n)]
for i in range(n):
    for j in Son_first[i]:
         for y in Son_first[j]:
            grandchildren[i].add(y)
def reqans(l):
    if reqanstable[l]:
        return reqanstable[l]
    if Son_first[l] == set():
        return 1
    else:
        value = max(1 + sum(map(reqans, grandchildren[l])), sum(map(reqans, Son_first[l])) )
        reqanstable[l] = value
        return value
    
print(reqans(a))       

            
            
        
        
        
        
        
        
    