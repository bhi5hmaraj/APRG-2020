#converts 1 dimensional coordinates into 2d coordinates
def dim(length, breadth, i, j):
    return ((i*breadth) + j)

#returns the number of bombs in the neighbourhood of a square
def bombsInNeighbourhood(inList, length, breadth, i, j):
    bombs = 0
    t = 0
    
    try:
        inList[dim(length, breadth, i-1, j-1)] == '*'
    except: 
        t = 0
    else:
        if (inList[dim(length, breadth, i-1, j-1)] == '*' and j%m != 0 and i != 0) :
            bombs += 1
            
    try:
        inList[dim(length, breadth, i-1, j)] == '*'
    except:
        t = 0
    else:
        if (inList[dim(length, breadth, i-1, j)] == '*' and i != 0) :
            bombs += 1
            
    try:
        inList[dim(length, breadth, i-1, j+1)] == '*'
    except:
        t = 0
    else:
        if (inList[dim(length, breadth, i-1, j+1)] == '*' and (j+1)%m != 0 and i != 0) :
            bombs += 1
            
    try:
        inList[dim(length, breadth, i, j-1)] == '*'
    except:
        t = 0
    else:
        if (inList[dim(length, breadth, i, j-1)] == '*' and j%m != 0) :
            bombs += 1
            
    try:
        inList[dim(length, breadth, i, j+1)] == '*'
    except:
        t = 0
    else:
        if (inList[dim(length, breadth, i, j+1)] == '*' and (j+1)%m != 0) :
            bombs += 1
            
    try:
        inList[dim(length, breadth, i+1, j-1)] == '*'
    except: 
        t = 0
    else:
        if (inList[dim(length, breadth, i+1, j-1)] == '*' and j%m != 0 and i != (n-1)) :
            bombs += 1
            
    try:
        inList[dim(length, breadth, i+1, j)] == '*'
    except:
        t = 0
    else:
        if (inList[dim(length, breadth, i+1, j)] == '*' and i != (n-1)) :
            bombs += 1
            
    try:
        inList[dim(length, breadth, i+1, j+1)] == '*'
    except:
        t = 0
    else:
        if (inList[dim(length, breadth, i+1, j+1)] == '*' and (j+1)%m != 0 and i != (n-1)) :
            bombs += 1
            
    return bombs
    
#returns the number of bombs in the neighbourhood if the square is not bombed, * otherwise
def neighbourhoodUpdate(inList, length, breadth, i, j):
    if inList[dim(length, breadth, i, j)] == '*' :
        return '*'
    else:
        return bombsInNeighbourhood(inList, length, breadth, i, j)

#print("tomato")
#list taking n amd m
li = list(map(int, input().split()))

#n and m denote the dimension of the minefield
n = li[0]
m = li[1]

#temporarily holds values
tempList = []

#inputList is the list containing .'s and *'s.
inputList = []

for i in range(0, n):
    tempList += list(map(str, input().split()))
    
for i in range(0, n) :
    inputList += tempList[i]

#neighbourhoodList contains info about number of bombs in the neighbourhood of a square
neighbourhoodList = []

t = ''

for i in range(0, n):
    if i != 0 :
        t = ''
        
    for j in range(0, m):
        neighbourhoodList.append(neighbourhoodUpdate(inputList, n, m, i, j))
        t += str(neighbourhoodList[dim(n, m, i, j)])
    print(t)



