n,d,r = map(int,input().split())
l1 = []
l2 = []
l1=l1+[int(x) for x in input().split()]
l2=l2+[int(x) for x in input().split()]
l1.sort()
l2.sort()
"""while(len(l1)<n):
    l1.append(0)
while(len(l2)<n):
    l2.append(0)"""
s = 0
for i in range(n):
    if l1[i]+l2[n-1-i] > d:
        s = s + ((l1[i]+l2[n-1-i])-d)*r
        #l1.remove(min(l1))
        #l2.remove(max(l2))
print(s)
#l=[2,3,1]
#l.sort()
#print(l)