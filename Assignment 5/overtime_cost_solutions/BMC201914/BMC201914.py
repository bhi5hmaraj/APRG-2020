(N, D, R)=map(int, input().split())
s1=0
s2=0

M=list(map(int, input().split()))
M.sort()
A=list(map(int, input().split()))
A.sort(reverse=True)

s=0        
for i in range(N):
    if M[i]+A[i]>D:
        s=s + R*((M[i]+A[i]) - D)
    
print(s)