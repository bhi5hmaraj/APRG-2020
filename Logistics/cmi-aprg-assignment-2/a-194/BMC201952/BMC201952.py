n = int(input())
l = []
for i in range(n):
    m=0
    n=0
    z = input().split()
    if (z[0]=='+'):
        l.append(int(z[1]))
        m = max(m,int(z[1]))
        n = min(n,int(z[1]))
    else:
        c=0
        for j in range(int(z[1]), 1 + int(z[2])):
            if (j in l):
                c+=1
        print(c)
