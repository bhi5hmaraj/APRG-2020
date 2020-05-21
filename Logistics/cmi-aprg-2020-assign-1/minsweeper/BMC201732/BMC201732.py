def split(word): 
    return [char for char in word]

def listToString(s):  
    str1 = ""  
    for ele in s:  
        str1 += str(ele)      
    return str1  

n, m = [int(x) for x in raw_input().split()] 
m_atrix = [[0 for y in range(m+2)] for x in range(n+2)]
for i in range(1,n+1):
    a = split(raw_input())
    for j in range(1,len(a)+1):
        if a[j-1] == "*":
            for x in range(i-1,i+2):
                for y in range(j-1,j+2):
                    if m_atrix[x][y] != "*":
                        m_atrix[x][y] += 1
            m_atrix[i][j] = "*"
mAtrix = [[0 for y in range(m)] for x in range(n)]
for x in range(n):
    for y in range(m):
        mAtrix[x][y] = m_atrix[x+1][y+1]
for x in range(n):
    print(listToString(mAtrix[x]))
    
    

