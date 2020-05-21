#this is the input string
inpstring = []

#list to be printed
printlist = ""

#number of rows and columns
rc = list(map(int , input().split()))
n = rc[0]
m = rc[1]

#taking the input field
for i in range(n):
    inpstring.append(input())

def adj(i , j):
    count = 0
    if (i < n and j + 1 < m and inpstring[i][j + 1] == "*"):
        count = count + 1
    if (i < n and j - 1 >= 0 and inpstring[i][j - 1] == "*"):
        count = count + 1
    if (i + 1 < n and j < m and inpstring[i + 1][j] == "*"):
        count = count + 1
    if (i - 1 >= 0 and j < m and inpstring[i - 1][j] == "*"):
        count = count + 1
    if (i + 1 < n and j + 1 < m and inpstring[i + 1][j + 1] == "*"):
        count = count + 1
    if (i + 1 < n and j - 1 >= 0 and inpstring[i + 1][j - 1] == "*"):
        count = count + 1
    if (i - 1 >= 0 and j + 1 < m and inpstring[i - 1][j + 1] == "*"):
        count = count + 1
    if (i - 1 >= 0 and j - 1 >= 0 and inpstring[i - 1][j - 1] == "*"):
        count = count + 1
    
    return count

for i in range(n):
    printlist = ""
    for j in range(m):
        if (inpstring[i][j] == "*"):
            printlist = printlist + "*"
        else:
            printlist = printlist + str(adj(i , j))
    print(printlist)
        
