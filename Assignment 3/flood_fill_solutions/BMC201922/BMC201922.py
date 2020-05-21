def func_1():
    A = [[0 for j in range(B)] for i in range(B)]
    for E_1 in L_1:
        j = E_1[0]
        i = E_1[1]
        A[j-1][i-1] += 2
    return (A)

def func_2(A):
   
    P = []
    A[S[0] - 1][S[1] - 1] = 1
    P.append(S)
    while(P):
        R = P.pop(0)
        a = R[0]
        b = R[1]
        Q = [[a - 1,b],[a,b - 1],[a + 1,b],[a,b + 1]]
        for E_2 in Q:
            p = E_2[0]
            q = E_2[1]
            if(0 < p <= B and 0 < q <= B and A[p-1][q-1] == 0):
                A[p-1][q-1] = 1
                P.append(E_2)
    F = 0           
    for m in range(B):
        for n in range(B):
            if(A[m][n] == 0):
                F += 1
                break
    if(F):
        return ("N")
    else:
        return ("Y")

L_0 = list(map(int,input().split()))
B = L_0[0]
C = L_0[1]
S = list(map(int,input().split()))
L_1 = []
for k in range(C):
    L_1.append(list(map(int,input().split())))
if(C != len(L_1)):
    C = len(L_1)
D = func_1()
if(S in L_1):
    print("N")
else:
    print(func_2(D))