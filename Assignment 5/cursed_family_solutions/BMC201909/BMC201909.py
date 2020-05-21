
class Vertex:

    def __init__(self, index):
        self.index = index
        self.noc = 0
        self.parent = None

    def __lt__(self, other):
        return self.noc < other.noc

    def __le__(self, other):
        return self.noc <= other.noc

    def __repr__(self):
        return f'{self.noc}'


class Heap:

    def __init__(self, nodes):
        self.items = nodes


    def _heapify_downward(self, index):
        items, n_nodes = self.items, len(self.items)

        curr_index = index
        while True:
            lindex = curr_index << 1
            rindex = lindex + 1

            min_index = curr_index
            if lindex < n_nodes and items[lindex] < items[min_index]:
                min_index = lindex
            if rindex < n_nodes and items[rindex] < items[min_index]:
                min_index = rindex

            if min_index == curr_index:
                return

            items[curr_index], items[min_index] = items[min_index], items[curr_index]
            items[curr_index].index, items[min_index].index = curr_index, min_index

            curr_index = min_index


    def _heapify_upward(self, index):
        items = self.items

        curr_index = index
        while curr_index > 1:
            pindex = curr_index >> 1

            if items[pindex] <= items[curr_index]:
                return

            items[curr_index], items[pindex] = items[pindex], items[curr_index]
            items[curr_index].index, items[pindex].index = curr_index, pindex

            curr_index = pindex


    def build_heap(self):
        last_parent_index = self.items[-1].index >> 1

        while last_parent_index > 0:
            self._heapify_downward(last_parent_index)
            last_parent_index -= 1


    def delete(self, index):
        items = self.items

        if len(items) < 2:
            return None

        if len(items) == 2 or index == len(items) - 1:
            item = items.pop()
            item.index = -1
            return item

        items[index], items[-1] = items[-1], items[index]
        items[index].index, items[-1].index = index, -1

        item = items.pop()

        pindex = index >> 1
        if pindex and (items[pindex] > items[index]):
            self._heapify_upward(index)
        else:
            self._heapify_downward(index)

        return item


    def update(self, index):
        self._heapify_upward(index)


    def pop(self):
        return self.delete(1)


class Graph:

    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.heap = None


    def create(self):
        nodes = [Vertex(index) for index in range(self.n_nodes + 1)]

        for i in range(self.n_nodes - 1):
            id1, id2 = [int(m) for m in input().split()]
            father, son = nodes[id1], nodes[id2]

            father.noc += 1
            son.parent = father

        self.heap = Heap(nodes)


    def get_along_members(self):
        heap = self.heap
        heap.build_heap()

        count = 0
        min_node = heap.pop()
        while min_node:
            # print(min_node)

            count += 1
            parent = min_node.parent

            if parent and parent.index > 0:
                if parent.parent and parent.parent.index > 0:
                    parent.parent.noc -= 1
                    heap.update(parent.parent.index)

                heap.delete(parent.index)

            min_node = heap.pop()

        return count


def main():

    # Read Line 1
    n_members = int(input())

    graph = Graph(n_members)

    # create the graph
    graph.create()

    min_members = graph.get_along_members()
    print(min_members)

if __name__ == '__main__':
    main()
