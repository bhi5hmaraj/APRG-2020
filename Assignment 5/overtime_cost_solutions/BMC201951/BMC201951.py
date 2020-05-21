n,d,r = map(int,input().split())
A=list(map(int,input().split()))
A.sort()
B=list(map(int,input().split()))
B.sort(reverse = True)
c=0
for i in range(n):
   q=A[i]+B[i]
   if q>d:
       c = c + (r*(q-d))
       
print(c)