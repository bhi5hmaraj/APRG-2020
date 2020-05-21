A=list(map(int,input().split()))
n=A[0]
d=A[1]
r=A[2]
B=list(map(int,input().split()))
C=list(map(int,input().split()))
D=[]
B.sort()
C.sort()
for i in range(n):
    D=[B[i]]+D
s=0    
for i in range(0,n):
    if D[i]+C[i]>d:
        s=s+D[i]+C[i]-d
print(s*r)        
    
    
    
    
    
    


    
    
