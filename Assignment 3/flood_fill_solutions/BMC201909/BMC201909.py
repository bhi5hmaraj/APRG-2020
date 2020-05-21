from collections import deque

class Node:

    WHITE = 0
    BLACK = 1
    GREEN = 2

    def __init__(self, row_index, column_index):
        self.row = row_index
        self.col = column_index
        self.color = Node.WHITE


    def __repr__(self):
        return f'{self.color}'


class Graph:

    def __init__(self, grid_size):
        self.size = grid_size
        self.nodes = [[Node(row, col) for col in range(grid_size)] for row in range(grid_size)]


    def set_node_color_black(self, row_index, col_index):
        self.nodes[row_index][col_index].color = Node.BLACK


    def get_neighbours(self, node):
        nbrs = []
        row, col = node.row, node.col

        if row:
            nbrs.append(self.nodes[row - 1][col])

        if col < self.size - 1:
            nbrs.append(self.nodes[row][col + 1])

        if row < self.size - 1:
            nbrs.append(self.nodes[row + 1][col])

        if col:
            nbrs.append(self.nodes[row][col - 1])

        return nbrs


    def print(self):
        for row in range(self.size):
            print(' '.join(repr(self.nodes[row][col]) for col in range(self.size)))


    def bfs(self, start_row_index, start_col_index):
        start = self.nodes[start_row_index][start_col_index]
        start.color = Node.GREEN
        count = 1

        que = deque([start])

        while que:
            curr = que.popleft()
            for nbr in self.get_neighbours(curr):
                if nbr.color == Node.WHITE:
                    nbr.color = Node.GREEN
                    count += 1
                    que.append(nbr)

        return count

def main():

    input_line_no = 0
    total_input_lines = 2

    graph = None
    n_black = 0

    while input_line_no < total_input_lines:
        input_line_no += 1

        values = input().split()
        val1, val2 = int(values[0]), int(values[1])

        if input_line_no == 1:
            n, b = val1, val2
            total_input_lines += b

            graph = Graph(n)

        elif input_line_no == 2:
            start_row_index, start_col_index = val1 - 1, val2 - 1

        else:
            if graph.nodes[val1 - 1][val2 - 1].color == Node.WHITE:
                graph.set_node_color_black(val1 - 1, val2 - 1)
                n_black += 1

    count = graph.bfs(start_row_index, start_col_index)

    if count + n_black == n*n:
        print('Y')
    else:
        print('N')

        
if __name__ == '__main__':
   main()
