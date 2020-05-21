def isBlack(s):
    if s[2]=='black':
        return(True)
    else:
        return(False)
    
def coo(s):
    return([s[0],s[1]])

def neigh(s,l):
    i=s[0]
    j=s[1]
    ls=[]
    for k in l:
        if (coo(k) == [i+1,j]) or (coo(k) == [i-1,j]) or (coo(k) == [i,j+1]) or (coo(k) == [i,j-1]):
            ls = ls + [k]
        else:
            ls=ls
    return(ls)



def greenify(grid, x, y, n):
#flodfilling
    faber=[]
    faber.append((x,y))
    while len(faber) !=0:
        (c,d) = faber.pop()
        grid[c][d] = "green"
        #Case Handling:
        #since squares o edges are baad
        
        if (c >0):
            if grid[c-1][d] == 'white':
                faber.append((c-1,d))
        if c <n-1:
            if grid[c+1][d] == 'white':
                faber.append((c+1,d))
        if d >0:
            if grid[c][d-1] == 'white':
                faber.append((c,d-1))
        if d <n-1:
            if grid[c][d+1] == 'white':
                faber.append((c,d+1))
                
def allTrue(l):
    if l ==[]:
        return(True)
    else:
        return(l[0] and allTrue(l[1:]))
    
def anyTrue(l):
    if l ==[]:
        return(False)
    else:
        return(l[0] or anyTrue(l[1:]))

def isBlocked(s,l):
    if allTrue(map(isBlack,neigh(s,l))):
        return(True)
    else:
        return(False)

def mapColour(c,l):
    if l==[]:
        return([])
    else:
        return([k+[c] for k in l])


ls=list(map(int,input().split()))
n = ls[0]
b = ls[1]

lss=list(map(int,input().split()))
anfang_x = lss[0]-1
anfang_y = lss[1]-1

blackSquares =[]
for i in range(b):
    l = list(map(int,input().split()))
    alpha = l[0]-1
    beta = l[1]-1
    blackSquares.append([alpha,beta])

if n == 1:
    print("Y")
    exit()

grid = [["white" for i in range(n)] for j in range(n)] 
for i in range(b):
    f = blackSquares[i][0]
    g = blackSquares[i][1]
    grid[f][g] = "black"

greenify(grid, anfang_x, anfang_y, n)

for m in range(n):
    for n in range(n):
        if grid[m][n] == "white":
            print("N")
            exit()

print("Y")