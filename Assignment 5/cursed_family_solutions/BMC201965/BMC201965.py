class node:
   
    def __init__(self,n):
        self.n = n
        self.sons = []
        self.max_gath = None
        
    def add_node(self,son):
        self.sons.append(son)

    def max_gathering(self):
        if self.max_gath == None:
            self.incl = 1
            for son in self.sons:
                for grandson in son.sons:
                    if grandson.max_gath == None:
                        self.incl += grandson.max_gathering()
                    else:
                        self.incl += grandson.max_gath
                
            self.excl = 0
            for son in self.sons:
                if son.max_gath == None:
                    self.excl += son.max_gathering()
                else:
                    self.excl += son.max_gath
            
            g = max(self.incl, self.excl)
            self.max_gath = g
            return g
            
        else:
            return self.max_gath
        
        



fm = int(input())
l = [node(k) for k in range(fm+1)]
root = list(range(1+fm))

for inp in range(1,fm):
    f,s = list(map(int, input().split()))
    l[f].add_node(l[s])
    root[s] = None
    
root[0] = None
index = 0
for i in root:
    if i != None:
        index = i

print(l[root[index]].max_gathering())