from collections import deque
from Task1 import Node
from Task1 import Graph


def breadth_first_search(graph, start, goal):
    if start == goal:
        return [start]
    

    queue = deque([[start]])  
    

    visited = set([start])
    
    while queue:

        path = queue.popleft()
        node = path[-1] 
        
        for neighbor in graph.adjacency_list[node]:
            if neighbor == goal:
                return path + [goal]
            
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                queue.append(new_path)
    
    return [] 


def depth_first_search(graph, start, goal):

    if start == goal:
        return [start]
    

    stack = [[start]]  

    visited = set([start])
    
    while stack:

        path = stack.pop()
        node = path[-1]  
        

        for neighbor in graph.adjacency_list[node]:
            if neighbor == goal:
                return path + [goal]
            
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                stack.append(new_path)
    
    return []  

#---Main:---
graph = Graph()


node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')

graph.add_node(node_a)
graph.add_node(node_b)
graph.add_node(node_c)
graph.add_node(node_d)


graph.add_edge(node_a, node_b)
graph.add_edge(node_a, node_c)
graph.add_edge(node_b, node_c)
graph.add_edge(node_c, node_d)


graph.print_graph()


bfs_path = breadth_first_search(graph, 'A', 'D')
print("BFS Path from A to D:", bfs_path)

dfs_path = depth_first_search(graph, 'A', 'D')
print("DFS Path from A to D:", dfs_path)
