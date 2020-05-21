import sys
sys.setrecursionlimit(1500)
arr1 = list(map(int,input().split()))
t1 = tuple(map(int,input().split()))
z = []
for i in range(1,arr1[1]+1):
    x = tuple(map(int,input().split()))
    z.append(x)
y = [(i,j) for i in range(1,arr1[1]+1) for j in range(1,arr1[1]+1)]
u = list(set(y)-set(z))
a = t1
v = []
def fun(x):
    if x in u:
        v.append(x)
    else:
        return
    fun((t1[0]+1,t1[1]))
    fun((t1[0],t1[1]+1))
    fun((t1[0]-1,t1[1]))
    fun((t1[0],t1[1]-1))
fun(a)
if v.sort() == y.sort():
    print("Y")
else:
    print("N")