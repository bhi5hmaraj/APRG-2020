n,d,r = map(int, input().split())

lm = list(map(int, input().split()))
lm.sort()

la = list(map(int, input().split()))
la.sort()
la.reverse()

AnsList = [0]*n

for i in range(n):
    if lm[i]+la[i] > d:
        AnsList[i] = (lm[i]+la[i]-d)*r

print(sum(AnsList))