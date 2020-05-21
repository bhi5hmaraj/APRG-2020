r , c = map(int,input().split())
z = []
k = 0
while k < r :
        l = input()
        z.append(l)
        k = k+1
def f(a,b):
        ret = 0;
        if 0<=a and a<r and 0<=b and b<c:
            u= str(z[a]) 
            if u[b]=='*' or u[b]=="*":
                ret = 1
            else:
                ret = 0
        else:
            ret = 0
        # print("f(%d, %d) = %d" % (a, b, ret))
        return ret
    
    
i=0
while i in range (0,r):
    l = 0
    d = ""
    q = str (z[i])
    # print(z[i])
    for l in range (0,c+1):
        if l==c :
            print (d)
            i+=1
            l=0
            break
        elif q[l] == '*' or q[l] == "*" :
            d=d +"*"
            l=l+1
        else :
            d=d + str(f(i,l+1)+f(i,l-1)+f(i+1,l-1)+f(i+1,l)+f(i+1,l+1)+f(i-1,l-1)+f(i-1,l)+f(i-1,l+1))
            l+=1
