from collections import deque

class Weights(dict):
    
    def __missing__(self, key):
        return ()
    
class Vertex:

    INIT_WEIGHT = 3 * 10**9

    def __init__(self, index):
        self.index = index
        self.neighbours = []
        self.weight = Vertex.INIT_WEIGHT
        self.weight2 = Vertex.INIT_WEIGHT + 1

    def update(self, w1, w2):
        wts = [self.weight, self.weight2, w1, w2]
        wts.sort()

        weight1, weight2 = wts[0], wts[0]
        wts = [w for w in wts if w > weight1]
        if wts: weight2 = wts[0]

        if self.weight == weight1 and self.weight2 == weight2:
            return False

        self.weight, self.weight2 = weight1, weight2
        return True

    def __repr__(self):
        return f'({self.index}, {self.weight}, {self.weight2})'


class Graph:

    def __init__(self):
        self.start = None
        self.end = None
        self.weights = Weights()

    def add_edges(self, n_vertices, edges):
        nodes = [Vertex(i) for i in range(n_vertices + 1)]
        self.start = nodes[1]
        self.end = nodes[n_vertices]

        for v1_index, v2_index, weight in edges:
            if v1_index > v2_index:
                v1_index, v2_index = v2_index, v1_index

            node_1, node_2 = nodes[v1_index], nodes[v2_index]
            node_1.neighbours.append(node_2)
            node_2.neighbours.append(node_1)

            self.weights[(v1_index, v2_index)] += (weight,)

        self.nodes = nodes


    def bfs(self):
        self.start.weight = 0
        self.start.weight2 = 0

        que = deque([self.start])
        while que:
            curr = que.popleft()
            # if curr.index == self.end.index:
            #     continue
            
            to_be_queued = []
            for nbr in curr.neighbours:
                id1, id2 = (curr.index, nbr.index) if curr.index < nbr.index else (nbr.index, curr.index)
                edge_weights = self.weights[(id1, id2)]

                for edge_weight in edge_weights:                
                    if nbr.update(curr.weight + edge_weight, curr.weight2 + edge_weight):
                        to_be_queued.append(nbr)

            if to_be_queued:
                to_be_queued.sort(key = lambda v: v.weight)
                que.extend(to_be_queued)

        return self.end.weight2

def main():

    # Read Line 1
    values = input().split()
    n_vertices, n_edges = int(values[0]), int(values[1])

    # Read the rest lines
    edges = [[int(v) for v in input().split()] for i in range(n_edges)]

    graph = Graph()
    graph.add_edges(n_vertices, edges)

    end_weight2 = graph.bfs()

    print(end_weight2)


if __name__ == '__main__':
    main()

