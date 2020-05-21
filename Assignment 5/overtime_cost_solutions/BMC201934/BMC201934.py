def run():
    a= list(map(int,input().split()))
    b= list(map(int,input().split()))
    c= list(map(int,input().split()))
    b.sort()
    c.sort()
    i=0
    sum=0
    while i<a[0]:
        if b[i]+c[a[0]-1-i]-a[1]>0:
            sum=sum+b[i]+c[a[0]-1-i]-a[1]
        i=i+1
    print(sum*a[2])
run()