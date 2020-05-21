#We store the list of black pixels as a list of 2 element lists#
#Always remember to deduct 1 from each coordinate#
#0 is White, 1 colored, 2 Black
#Do BFS or DFS

def initialize():
    M = [[0 for i in range(N)] for j in range(N)]
    
    for elem in list1:
        i = elem[0]
        j = elem[1]
        M[i-1][j-1]+=2
    return (M)

def floodfill(M):
   
    q = []
    M[initpt[0]-1][initpt[1]-1] = 1
    q.append(initpt)
    while(q):
        z = q.pop(0)
        i = z[0]
        j = z[1]
        nbr = [[i-1,j],[i,j-1],[i+1,j],[i,j+1]]
        for elem in nbr:
            a = elem[0]
            b = elem[1]
            if(0<a<=N and 0<b<=N and M[a-1][b-1] == 0):
                M[a-1][b-1] = 1
                q.append(elem)
    count = 0           
    for i in range(N):
        for j in range(N):
            if(M[i][j] == 0):
                count += 1
                break
    if(count):
        return ("N")
    else:
        return ("Y")
    
    

L = list(map(int,input().split()))
N = L[0]
B = L[1]
initpt = list(map(int,input().split()))
list1 = []
for i in range(B):
    list1.append(list(map(int,input().split())))
if(B != len(list1)):
    B = len(list1)
K = initialize()
if(initpt in list1):
    print("N")
else:
    print(floodfill(K))


    


    
    
    
    