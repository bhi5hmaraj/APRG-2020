inp = list (map (int,input().split()))
m = inp[0]
n = inp[1]
X = []
for i in range(m):
    inp = '.'+input()+'.'
    X.append(list(inp))
B=[]
for i in range (n+2):
    B.append('.')
X=[B]+X+[B]
Y = []
for i in range (1,m+1):
    inp = []
    for j in range (1,n+1):
        val = 0
        if ((X[i])[j]=='*'):
            val = '*'
        else:
            if((X[i-1])[j]=='*'):
                val = val+1
            if((X[i-1])[j-1]=='*'):
                val = val+1
            if((X[i-1])[j+1]=='*'):    
                val=val+1
            if((X[i])[j+1]=='*'):
                val=val+1
            if((X[i])[j-1]=='*'):
                val=val+1
            if((X[i+1])[j-1]=='*'):        
                val=val+1
            if((X[i+1])[j]=='*'):
                val=val+1
            if((X[i+1])[j+1]=='*'):    
                val=val+1
        inp.append(val)
    Y.append(inp)        
for i in Y:
    for j in i: print(j,end = '')
    print()
