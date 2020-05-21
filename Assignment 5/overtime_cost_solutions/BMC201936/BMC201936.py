#n,d,r are values as given in the question.
n,d,r=map(int, input().split())

list1=list(map(int,input().split()))
list2=list(map(int,input().split()))

list2.sort(reverse=True)
list1.sort()

OVERTIME=0
for k in range(n):
    cost=(list2[k]+list1[k])
    if cost > d:
        OVERTIME += (cost-d)*r
print(OVERTIME)
