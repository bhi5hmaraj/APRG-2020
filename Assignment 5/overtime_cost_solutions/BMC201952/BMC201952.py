n,d,r=map(int, input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort()
B.sort(reverse=True)
overtime=0
for i in range(n):
    cost=(A[i]+B[i])
    if cost > d:
        overtime += r*(cost-d)
print(overtime)