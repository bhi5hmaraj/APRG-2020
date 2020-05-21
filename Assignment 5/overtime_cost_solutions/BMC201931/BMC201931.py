n,d,r=map(int, input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort()
B.sort(reverse=True)
sum1=0
for i in range(n):
    sum2=A[i]+B[i]
    if sum2 > d:
        sum1=sum1+(sum2-d)*r
    else:
        continue
print(sum1)