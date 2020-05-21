from collections import deque

not_reachable = 'IMPOSSIBLE'

class Vertex:

    MAX_COST = 10**5

    def __init__(self, sp_index, stop_index):
        self.sp_index = sp_index
        self.index = stop_index
        self.neighbours = []
        self.weight = Vertex.MAX_COST
    
    def __repr__(self):
        return f'({self.index}, {self.weight}, {self.sp_index}, {[v.index for v in self.neighbours]})'


class Graph:

    def __init__(self, n_sp, time_list, destination):
        self.start = None
        self.dest_index = destination
        self.destinations = []
        self.n_sp = n_sp
        self.times = time_list
    
    def add_stops(self, stops_list):
        all_vertices = []
        start_nodes = []

        for sp_no, stops in enumerate(stops_list):
            vertices = [Vertex(sp_no, stop) for stop in stops]
            all_vertices.append(vertices)
            self.destinations.extend([v for v in vertices if v.index == self.dest_index])
            start_nodes.append(vertices[0])

            for i in range(len(vertices) - 1):
                vertices[i].neighbours.append(vertices[i + 1])
                vertices[i + 1].neighbours.append(vertices[i])

        for i in range(len(all_vertices) - 1):
            for j in range(i+1, (len(all_vertices))):
                common = [(v1, v2) for v1 in all_vertices[i] for v2 in all_vertices[j] if v1.index == v2.index]

                if common and common[0][0].index == 0:
                    common.pop(0)

                for v1, v2 in common:
                    v1.neighbours.append(v2)
                    v2.neighbours.append(v1)

        starts = [node for node in start_nodes if node.index == 0]
        self.start = Vertex(-1, -1)
        self.start.neighbours.extend(starts)


    def get_weight(self, v1, v2):
        if v1.sp_index == v2.sp_index:
            diff = (v1.index - v2.index) if v1.index > v2.index else (v2.index - v1.index)
            return diff*self.times[v1.sp_index] 

        if v1.index == v2.index:
            return 60

        if v1.sp_index == -1 or v2.sp_index == -1:
            return 0      


    def bfs(self):
        self.start.weight = 0

        que = deque([self.start])

        while que:
            curr = que.popleft()

            for nbr in curr.neighbours:
                nbr_weight = curr.weight + self.get_weight(curr, nbr)

                if nbr.weight > nbr_weight:
                    nbr.weight = nbr_weight
                    que.append(nbr)


        return min(v.weight for v in self.destinations) if self.destinations else Vertex.MAX_COST


def main():

    # Read Line 1
    values = input().split()
    n_sp, destination = int(values[0]), int(values[1])

    # Read Line 2
    time_list = [int(data) for data in input().split()]

    graph = Graph(n_sp, time_list, destination)

    # Read the rest lines
    input_line_no = 0
    stops_list = []
    while input_line_no < n_sp:
        input_line_no += 1
        stops_list.append([int(data) for data in input().split()])

    graph.add_stops(stops_list)

    cost = graph.bfs()

    print(cost if cost < Vertex.MAX_COST else not_reachable) 


if __name__ == '__main__':
    main()
