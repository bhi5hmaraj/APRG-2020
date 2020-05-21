while True:
    inp = input().split()
    n = int(inp[0])
    d = int(inp[1])
    r = int(inp[2])

    if n == 0 and d == 0 and r == 0:
        break
    
    morn = []
    inp = input().split()
    for i in inp:
        morn.append(int(i))
    morn.sort()

    aft = []
    inp = input().split()
    for i in inp:
        aft.append(int(i))
    aft.sort(reverse=True)

    cost = 0
    for i in range(n):
        c = morn[i] + aft[i]
        if c > d:
            cost += ((c-d)*r)
    
    print(cost)
