Q = int(input())
mylist = []
for i in range(Q):
    inp = input()
    l_inp = inp.split()
    if len(l_inp) == 2:
        mylist.append(int(l_inp[1]))
    mylist.sort()
#    def ans(inp):
#        if len(l_inp) != 2:
#            return (len([i for i in mylist if int(l_inp[1]) <= int(i) and int(i) <= int(l_inp[2])]))
#        else:
#            inp = input()
        
    if len(l_inp) != 2:
        list1 = [i for i in mylist if int(l_inp[1]) <= int(i) and int(i) <= int(l_inp[2])]
        temp = []
        for x in list1:
            if x not in temp:
                temp.append(x)
        list1 = temp
        print (len(list1))
    
    #len(None) = '\n'
#    print(mylist)
    #if len(l_inp) == 2:
#    print((ans(inp)))
