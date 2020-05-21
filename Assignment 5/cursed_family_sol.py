from collections import deque

class Node:
    def __init__(self, l):
        self.l = l
        self.children = []
        self.parent = None

    def add_child(self, c):
        self.children.append(c)

    def set_parent(self, p):
        self.parent = p

class Tree:
    def __init__(self):
        self.root = None
        self.nodes = {}
    
    def get_node(self, n):
        if n not in self.nodes:
            self.nodes[n] = Node(n)
        return self.nodes[n]

    def find_root(self):
        for n, node in self.nodes.items():
            if node.parent is None:
                self.root = node
                break

    def max_is(self):
        stack = deque()
        stack.append(self.root)

        post_order = deque()

        while len(stack) != 0:
            cur = stack.pop()
            post_order.appendleft(cur)
            for c in cur.children:
                stack.append(c)

        max_is = {}
        for n in post_order:
            keep = 1
            for s in n.children:
                for g in s.children:
                    keep += max_is[g.l]
            leave = 0
            for s in n.children:
                leave += max_is[s.l]
            max_is[n.l] = max(keep,leave)
        
        return max_is[self.root.l]


if __name__ == "__main__":
    
    n = int(input())
    t = Tree()
    for i in range(n-1):
        i = input()
        tmp = i.split()
        u = int(tmp[0])
        v = int(tmp[1])
        u_node = t.get_node(u)
        v_node = t.get_node(v)
        u_node.add_child(v_node)
        v_node.set_parent(u_node)
    
    t.find_root()
    print(t.max_is())