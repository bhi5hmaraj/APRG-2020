import sys
sys.setrecursionlimit(10**6)
K,b=input().split()
K,b=int(K),int(b)
x,y=input().split()
x,y=int(x),int(y)
s = [[1] * (K+2)] + [[1] + [0] * K + [1] for i in range(K)] + [[1] * (K+2)] #black border to avoid base cases
for i in range(b):
    k,l=input().split()
    k,l=int(k),int(l)
    s[k][l] = 1 #1 represents the colour black
    
floodedlist = [(x,y)]
s[x][y] = 2     #2 represents the colour blue
while floodedlist:
    filledlist = []
    for (m, n) in floodedlist:
        neighbours = [(m+1,n),(m-1,n),(m,n+1),(m,n-1)]
        for (p,q) in neighbours:
            if not s[p][q]:
                s[p][q] = 2
                filledlist.append((p,q))
    floodedlist = filledlist[:]
    
Remaining_White_pixels = []
for line in s:
    if 0 in line:
        Remaining_White_pixels.append(1)
        
if Remaining_White_pixels:
    print("N")
else:
    print("Y")