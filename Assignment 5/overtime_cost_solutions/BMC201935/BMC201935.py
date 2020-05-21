input1 = [int(x) for x in input().split()]
n = input1[0]
d = input1[1]
r = input1[2]
morn = [int(x) for x in input().split()]
morning = sorted(morn)
even = [int(x) for x in input().split()]
evening = sorted(even)
isum = 0
newsum = 0
printsum = 0
for i in range(0,n):
    isum = morning[i] + evening[n-1-i]
    if isum > d:
        newsum = isum*r - d*r
    else:
        newsum = 0
    printsum += newsum    
print(printsum) 