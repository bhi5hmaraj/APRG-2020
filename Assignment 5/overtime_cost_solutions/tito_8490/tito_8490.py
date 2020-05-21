listItems = input()
myList = listItems.split(" ")
n = int(myList[0])
d = int(myList[1])
r = int(myList[2])
listItems = input()
myList = listItems.split(" ")
mor = []
for i in range(0, n):
    mor.append(int(myList[i]))
listItems = input()
myList = listItems.split(" ")
eve = []
for i in range(0, n):
    eve.append(int(myList[i]))
mor.sort()
eve.sort()
s = 0
for i in range(0, n):
    hour = mor[i]+eve[n-1-i]
    if hour > d:
        s += r * (hour - d)
print(s)