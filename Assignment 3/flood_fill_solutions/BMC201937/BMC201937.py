import array          
        
def floodfill(x,y,N):
    global AdjMatrix
    global Visited
    global counter 
    if(x > N-1 or y > N-1):
        return 
    if(x < 0 or y < 0):
        return 
    if(Visited[(N*x)+y] == 1):
        return 
    Visited[(N*x)+y] = 1
    if(AdjMatrix[(N*x)+y] == -1):
        return 
    counter = counter+1;
    floodfill(x+1, y, N)
    floodfill(x-1, y, N)
    floodfill(x, y+1, N)
    floodfill(x, y-1, N)
    return

def wrapper_func():
#N is cardinality of matrix
    global AdjMatrix
    global Visited
    global counter 
    N1 , b1  = input().split()
    N = int(N1)
    invalid =0  
    tmplist1 = [int(1)]*(N*N)
    AdjMatrix = array.array('i',tmplist1)
    #AdjMatrix = [[int(1)]*N]*N 
    tmplist = [int(0)]*(N*N)
    Visited = array.array('i',tmplist)

#b is no of black nodes
    b = int(b1)
    
    if (b > N*N) :
        b = N*N
        invalid = 1
       
    

#(x,y) is starting white pixel
    x1,y1 = input().split()
    x = int(x1)

    y = int(y1)

    if (b == 0):
        print ('Y')
        exit()
    unique_b = b
    for i in range(b):
        s1,s2 = input().split()
        bi = int(s1)
        bj = int(s2)
        if (bi == x and bj == y):
            invalid = 1
        if (AdjMatrix[(bi-1)*N+(bj-1)] == -1):
            unique_b= unique_b-1
        AdjMatrix[(bi-1)*N+(bj-1)] = -1  
        
    if (invalid == 1):
        print ('N')
        exit()

    counter = 0
    expected_counter = (N*N)-unique_b

    floodfill(x-1,y-1,N)


    if (counter == expected_counter):
        print('Y')
    else:
        print('N')
        
wrapper_func()