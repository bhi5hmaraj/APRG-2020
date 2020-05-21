l1=list(map(int,input().split()))
n=l1[0]
d=l1[1]
r=l1[2]
l2=list(map(int,input().split()))
l3=list(map(int,input().split()))
def mergeSort(l):
    if len(l) > 1:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              l[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                l[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            l[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            l[k]=right[j]
            j += 1
            k += 1
    return l        

#myList = [54,26,93,17,77,31,44,55,20]
#p=mergeSort(l1)
#print(p)
p1=mergeSort(l2)
p2=mergeSort(l3)
p=[]
for i in range (n):
    p.append(p1[i]+p2[n-i-1])
counter=0
for i in range (n):
    if p[i]>d:
        counter=counter+(p[i]-d)*r
print(counter)        
    
