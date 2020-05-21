n, d, r = map(int, input().split())
Jobs = [] 
for i in range(2):
    Jobs.append(list(map(int, input().split())))

Jobs[0].sort()
Jobs[1].sort(reverse = True)

t = 0
for i in range(n):
    if Jobs[0][i] + Jobs[1][i] > d:
        t = t + Jobs[0][i] + Jobs[1][i] - d
        
print(t*r)
