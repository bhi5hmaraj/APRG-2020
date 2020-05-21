import sys
n = int(sys.argv[1])
f = open('input.txt', 'w')  
print(n, file=f) 
print('\n'.join(map(lambda x : '+ %d' % x, range(1, n + 1))), file=f) 
f.close() 
