num_workers, max_day, over_cost = list(map(int, input().split()))
morn_work = list(map(int, input().split()))
even_work = list(map(int, input().split()))
morn_work.sort()
even_work.sort()
even_work = even_work[::-1]

tot_work = [0 for i in range(num_workers)]
for i in range(num_workers):
    tot_work[i] = morn_work[i] + even_work[i]
  
payable = 0
for i in range(num_workers):
    if tot_work[i] <= max_day:
        payable += 0
    elif tot_work[i] > max_day:
        payable += (tot_work[i] - max_day)*over_cost

print(payable)