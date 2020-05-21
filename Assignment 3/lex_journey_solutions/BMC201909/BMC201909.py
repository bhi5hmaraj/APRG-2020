from collections import deque
from operator import attrgetter

class Vertex:

    INIT_DIST = -1

    def __init__(self, idx):
        self.index = idx
        self.distance = Vertex.INIT_DIST
        self.neighbours = []
        self.sp_neighbours = []


    def __eq__(self, other):
        return self.index == other.index


    def __hash__(self):
        return hash(self.index)


    def __repr__(self):
        return f'Vertex: {self.index}, {self.distance}, {[x.index for x in self.neighbours]}, {self.sp_neighbours}'


class Graph:

    def __init__(self):
        self.nodes = None
        self.ranks = {}


    def create(self, n_vertices):
        Vertex.INIT_DIST = 2 * n_vertices
        self.nodes = [Vertex(i) for i in range(n_vertices + 1)]


    def add_edge(self, v1_index, rank, v2_index):
        if v1_index > v2_index:
            v1_index, v2_index = v2_index, v1_index

        node_1, node_2 = self.nodes[v1_index], self.nodes[v2_index]
        node_1.neighbours.append(node_2)
        node_2.neighbours.append(node_1)

        self.ranks[(v1_index, v2_index)] = rank


    def rank(self, v1, v2):
        idx1, idx2 = (v1.index, v2.index) if v1.index < v2.index else (v2.index, v1.index)
        return self.ranks[(idx1, idx2)]

    def print(self):
        for v in self.nodes:
            print(v)


    def bfs(self, first, last):
        start = self.nodes[first]
        start.distance = 0
        
        que = deque([start])
        while que:
            curr = que.popleft()

            nbr_dist = curr.distance + 1
            for nbr in curr.neighbours:
                if nbr.distance > nbr_dist:
                    nbr.distance = nbr_dist
                    que.append(nbr)
                    if nbr.index == last:
                        return True

        return False


    def nodes_in_shortest_paths(self, first, last):
        end = self.nodes[last]

        curr_nodes = [end]
        adj_nodes = set()
        curr_dist, adj_dist = end.distance, (end.distance - 1)

        while curr_dist > 0:
            for node in curr_nodes:
                for i in range(len(node.neighbours)):
                    nbr = node.neighbours[i]
                    if nbr.distance == adj_dist:
                        node.sp_neighbours.append(i)
                        nbr.sp_neighbours.append(nbr.neighbours.index(node))

                        adj_nodes.add(nbr)

            curr_nodes = adj_nodes
            adj_nodes = set()
            curr_dist, adj_dist = adj_dist, (adj_dist - 1)


    def required_path(self, first, last):

        rank_list = []

        start, end = self.nodes[first], self.nodes[last]

        nodes = [start]
        node_distance = 0
        while node_distance < end.distance:
            node_distance += 1
            all_sp_nbrs = {(node, sp_nbr, self.rank(node, sp_nbr)) for node in nodes for sp_nbr in [node.neighbours[index]
                for index in node.sp_neighbours] if sp_nbr.distance == node_distance}
                
            if not all_sp_nbrs:
                break

            edge = min(all_sp_nbrs, key = lambda x: x[2])
            rank_list.append(edge[2])

            nodes = {e[1] for e in all_sp_nbrs if e[2] == edge[2]}

        return rank_list


def main():

    # Read Line 1
    values = input().split()
    n_vertices, n_edges = int(values[0]), int(values[1])

    graph = Graph()
    graph.create(n_vertices)

    # Read Line 2
    values = input().split()
    start, end = int(values[0]), int(values[1])

    input_line_no = 0
    while input_line_no < n_edges:
        input_line_no += 1
        values = input().split()
        val1, rank, val2 = int(values[0]), values[1], int(values[2])
        graph.add_edge(val1, rank, val2)

    if not graph.bfs(start, end):
        print('No path')
        return
    
    graph.nodes_in_shortest_paths(start, end)
    rank_list = graph.required_path(start, end)

    print(''.join(rank_list))


if __name__ == '__main__':
    main()
