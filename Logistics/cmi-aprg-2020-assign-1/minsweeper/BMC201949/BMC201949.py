l=map(int,raw_input().split())
n=l[0]
m=l[1]
fld=[]
for i in range(0,n):
    line=map(str,raw_input())
    fld=fld+[line]
hint=[]
for i in range(n+2):
    hint=hint+[[0]*(m+2)]
for i in range(n):
    for j in range(m):
        if(fld[i][j]=='*'):
            hint[i+1][j+1]='*'
for i in range(1,n+1):
    for j in range(1,m+1):
        if (hint[i][j]!='*'):
            check=[hint[i+1][j+1],hint[i-1][j-1],hint[i+1][j-1],hint[i-1][j+1],hint[i][j+1],hint[i+1][j],hint[i-1][j],hint[i][j-1]]
            c=0
            for z in range(8):
                if(check[z]=='*'):
                    c=c+1
            hint[i][j]=c        
        
        
        
        
for x in range(1,n+1):
    stir=""
    for y in (hint[x][1:m+1]):
        stir=stir+str(y)
    print(stir)    


             
            



    
            
            
    
              

                    
                
            
                   
            
        
               
    
    
       
        
    




