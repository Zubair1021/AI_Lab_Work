class Node:
    def __init__(self, name):
        self.name = name

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        if node.name not in self.adjacency_list:
            self.adjacency_list[node.name] = []

    def add_edge(self, node1, node2):
        if node1.name in self.adjacency_list and node2.name in self.adjacency_list:
            self.adjacency_list[node1.name].append(node2.name)
            self.adjacency_list[node2.name].append(node1.name)

    def delete_edge(self, node1, node2):
        if node1.name in self.adjacency_list and node2.name in self.adjacency_list:
            if node2.name in self.adjacency_list[node1.name]:
                self.adjacency_list[node1.name].remove(node2.name)
            if node1.name in self.adjacency_list[node2.name]:
                self.adjacency_list[node2.name].remove(node1.name)

    def print_graph(self):
        for node in self.adjacency_list:
            print(node, ":", self.adjacency_list[node])

    def get_connected_nodes(self, node):
        return self.adjacency_list.get(node.name, [])

    def get_edge(self, node1, node2):
        if node2.name in self.adjacency_list.get(node1.name, []):
            return (node1.name, node2.name)
        return None

    def are_connected(self, node1, node2):
        return node2.name in self.adjacency_list.get(node1.name, [])

    def is_valid_path(self, path):
        for i in range(len(path) - 1):
            if path[i+1] not in self.adjacency_list.get(path[i], []):
                return False
        return True
    
    
    

# ---Main---:
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")

graph = Graph()
graph.add_node(nodeA)
graph.add_node(nodeB)
graph.add_node(nodeC)
graph.add_node(nodeD)

graph.add_edge(nodeA, nodeB)
graph.add_edge(nodeB, nodeC)
graph.add_edge(nodeD, nodeC)

graph.print_graph()

print(graph.get_connected_nodes(nodeD))  # Output: ['C']
print(graph.get_edge(nodeA, nodeB))      # Output: ('A', 'B')
print(graph.are_connected(nodeB, nodeC)) # Output: True
print(graph.is_valid_path(["C", "B", ""])) # Output: True
