
DEFAULT_WT = (10**7) + 1

class Vertex:

    def __init__(self, index):
        self.index = index
        self.neighbours = []
        self.parent = None
        self.ancestors = []
      
    def __repr__(self):
        return f'{self.index}'


class Graph:

    def __init__(self):
        self.weights = {}

    def add_edges(self, n_vertices, edges):
        nodes = [Vertex(i) for i in range(n_vertices + 1)]

        for v1_index, v2_index, weight in edges:
            if v1_index > v2_index:
                v1_index, v2_index = v2_index, v1_index

            node_1, node_2 = nodes[v1_index], nodes[v2_index]
            node_1.neighbours.append(node_2)
            node_2.neighbours.append(node_1)

            self.weights[(v1_index, v2_index)] = weight

        self.nodes = nodes.copy()
        self.graph = nodes[2:]

        start = nodes[1]
        start.ancestors.append(start)
        self.mst = [start]

    def extract_min(self):
        req_vertex, prev_vertex, min_wt = None, None, DEFAULT_WT

        for vertex in self.mst:
            for nbr in vertex.neighbours:
                if nbr in self.graph:
                    id1, id2 = (vertex.index, nbr.index) if vertex.index < nbr.index else (nbr.index, vertex.index)
                    if self.weights[(id1, id2)] < min_wt:
                        req_vertex, prev_vertex, min_wt = nbr, vertex, self.weights[(id1, id2)]

        return req_vertex, prev_vertex               


    def create_mst(self):
        while self.graph:
            vertex, prev_vertex = self.extract_min()

            self.graph.remove(vertex)
            self.mst.append(vertex)
            vertex.parent = prev_vertex
            vertex.ancestors = [vertex, prev_vertex]
            vertex.ancestors.extend(prev_vertex.ancestors)

            # print(vertex, prev_vertex)


    def truck_driving(self, queries):
        for first, last in queries:
            start = self.nodes[first]
            destination = self.nodes[last]

            common = None
            for v1 in start.ancestors:
                for v2 in destination.ancestors:
                    if v1 == v2:
                        common = v1
                        break
                if common:
                    break

            weights = []

            curr = start
            parent = curr.parent
            while curr != common:
                id1, id2 = (curr.index, parent.index) if curr.index < parent.index else (parent.index, curr.index)
                weights.append(self.weights[(id1, id2)])
                curr = parent
                parent = curr.parent

            curr = destination
            parent = curr.parent
            while curr != common:
                id1, id2 = (curr.index, parent.index) if curr.index < parent.index else (parent.index, curr.index)
                weights.append(self.weights[(id1, id2)])
                curr = parent
                parent = curr.parent
               
            print(max(weights))


def main():

    # Read Line 1
    values = input().split()
    n_vertices, n_edges = int(values[0]), int(values[1])

    graph = Graph()

    # Read the edges
    edges = [[int(v) for v in input().split()] for i in range(n_edges)]

    graph.add_edges(n_vertices, edges)
    graph.create_mst()

    # read no. of queries
    n_queries = int(input())

    # read the queries
    queries = [[int(v) for v in input().split()] for i in range(n_queries)]
    graph.truck_driving(queries)
    

if __name__ == '__main__':
    main()