# Enter your code here. Read input from STDIN. Print output to STDOUT
L=map(int,raw_input().split())
n = L[0]
m = L[1]
board = [[0] * (m+2)]
for i in range(n):
    a= map(str,raw_input())
    a=[0]+a+[0]
    board.append(a)
board += [[0] * (m+2)]

for row in range(1,n+1):
    for col in range(1,m+1):
        if(board[row][col] == '*'):
            board[row][col] = 1;
        else:
            board[row][col] = 0;

for i in range(1,n+1):
    temp = ""
    for j in range(1,m+1):
        if(board[i][j] == 1):
            temp2 = "*"
        else:
            temp2 = board[i-1][j-1]+board[i-1][j]+board[i-1][j+1]+board[i][j-1]+board[i][j+1]+board[i+1][j-1]+board[i+1][j]+board[i+1][j+1]
        temp += str(temp2)
    print(temp)
            
                        
            
            
