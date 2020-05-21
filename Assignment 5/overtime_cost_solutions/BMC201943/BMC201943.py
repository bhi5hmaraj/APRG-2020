first_List = list(map(int,input().split()))
n = first_List[0]
d = first_List[1]
r = first_List[2]
morning_List = list(map(int,input().split()))
morning_List.sort()

afternoon_List = list(map(int,input().split()))
afternoon_List.sort()
afternoon_List.reverse()

answer = 0
for i in range(n):
    duckyou = max (morning_List[i] + afternoon_List[i] - d,0)
    answer = answer + duckyou
ans = r * answer
print (ans)