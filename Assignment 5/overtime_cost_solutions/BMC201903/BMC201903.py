(n,d,r)= list(map (int,input().split()))
morning = list(map (int,input().split()))
afternoon = list(map (int,input().split()))
morning.sort()
afternoon.sort(reverse=True)
extra_hours= []
for i in range(n):
    extra_hours= extra_hours + [(morning[i]+afternoon[i])-d]

extra_pay = []
for i in range(n):
    if extra_hours[i]>0:
        extra_pay += [extra_hours[i]*r]
    else:
        extra_pay = extra_pay
       
print(sum(extra_pay))
            