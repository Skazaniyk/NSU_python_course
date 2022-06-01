class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.matrix = [[0 for _ in range(len(nodes))] for _ in range(len(nodes))]

    @property
    def adjacency_matrix(self):
        for elements in range(len(nodes)):
            self.matrix[elements][elements] = 1
            for neigbs in nodes[elements].neigbs:
                self.matrix[elements][neigbs] = 1
                self.matrix[neigbs][elements] = 1
        return print(self.matrix)

    @property
    def print_adjacency_matrix(self):
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                print(str(self.matrix[i][j]), end=" ")
            print()
        return self.matrix

    def is_connected(self, node_1, node_2):
        for i, node in enumerate(nodes):
            if node.value == node_1.value:
                id_1 = i
            if node.value == node_2.value:
                id_2 = i
        return self.is_connected_by_id(id_1, id_2)

    def is_connected_by_id(self, id_1, id_2):
        return bool(self.matrix[id_1][id_2])

    def get_node(self, id_):
        return self.nodes[id_]


class Node:
    def __init__(self, value, neigbs):
        self.value = value
        self.neigbs = neigbs


nodes = [
    Node(value='123', neigbs=[1, 2]),
    Node(value='13', neigbs=[0]),
    Node(value='321', neigbs=[0]),
]

graph = Graph(nodes)

graph.adjacency_matrix
graph.print_adjacency_matrix

node_1 = graph.get_node(0)
node_2 = graph.get_node(1)
node_3 = graph.get_node(2)

print(graph.is_connected(node_1, node_2))
print(graph.is_connected_by_id(1, 2))