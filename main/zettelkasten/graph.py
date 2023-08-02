class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = []

    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        if node2 not in self.edges[node1]:
            self.edges[node1].append(node2)
        if node1 not in self.edges[node2]:
            self.edges[node2].append(node1)

    def get_nodes(self):
        return self.nodes.keys()

    def get_edges(self):
        return [(node, neighbour) for node in self.nodes for neighbour in self.edges[node]]

    def get_neighbours(self, node):
        return self.edges[node] if node in self.edges else []