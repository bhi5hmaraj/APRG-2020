'''
Q = int(input())
mylist = []
for i in range(Q):
    inp = input()
    l_inp = inp.split()
    if len(l_inp) == 2:
        mylist.append(int(l_inp[1]))
    mylist.sort()

    def binary_search(A, l, h, k):
        if h >= l:
            mid = l + (h - l)//2
            if A[mid] == k:
                return 'YES'
            elif A[mid] > k:
                return binary_search(A, l, mid-1, k)
            else:
                return binary_search(A, mid+1, h, k)
        else:
            return 'NO'
        
    if len(l_inp) != 2:
        A = range(int(l_inp[1]), int(l_inp[2]) + 1)
        l = 0
        h = len(A) - 1
        list1 = [i for i in mylist if binary_search(A, l, h, i) == 'YES']     #int(l_inp[1]) <= int(i) <= int(l_inp[2])]
        temp = []
        for x in list1:
            if x not in temp:
                temp.append(x)
        list1 = temp
        print (len(list1))
'''
import sys
Q = int(input())
mylist = []
for i in range(Q):
    inp = input()
    l_inp = inp.split()
    if len(l_inp) == 2:
        mylist.append(int(l_inp[1]))
    mylist.sort()

    if len(l_inp) != 2:
        list1 = [i for i in mylist if int(l_inp[1]) <= int(i) and int(i) <= int(l_inp[2])]
        temp = []
        for x in list1:
            if x not in temp:
                temp.append(x)
        list1 = temp
        print (len(list1))