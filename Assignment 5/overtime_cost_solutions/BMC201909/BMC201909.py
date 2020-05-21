
def overtime_cost(n_workers, n_hours, overtime_charge, morning, afternoon):
    morning.sort()
    afternoon.sort(reverse = True)

    sum_list = [sum(v) for v in zip(morning, afternoon)]

    s = 0
    for n in sum_list:
        if n > n_hours:
            s += n - n_hours

    return s*overtime_charge



def main():

    # Read Line 1
    n_workers, n_hours, overtime_charge  = [int(v) for v in input().split()]

    # Read the next 2 lines
    morning = [int(m) for m in input().split()]
    afternoon = [int(m) for m in input().split()]

    print(overtime_cost(n_workers, n_hours, overtime_charge, morning, afternoon))
    

if __name__ == '__main__':
    main()