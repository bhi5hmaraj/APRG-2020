#taking the numbers
inp = list(input().split())
n , d , r = int(inp[0]) , int(inp[1]) , int(inp[2])

#taking the work
inp1 = list(input().split())
inp2 = list(input().split())
morning = []
afternoon = []
for i in range(n):
    morning.append(int(inp1[i]))
    afternoon.append(int(inp2[i]))
morning.sort()
afternoon.sort(reverse = True)

cost = 0
for i in range(n):
    p = morning[i] + afternoon[i]
    if (p > d):
        cost += r * (p - d)
print(cost)