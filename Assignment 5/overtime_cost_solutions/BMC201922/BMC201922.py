A = list(map(int, input().split())) 
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())), reverse = True) 
n = A[0]
r = A[2]
str_val = 0

def max_ovt(i):
    def ovt(i):
        return B[i] + C[i] - A[1]
    if (ovt(i) > 0) == True:
        return ovt(i)
    else:
        return 0

for i in range(n):
    str_val = str_val + r * max_ovt(i)
print(str_val)