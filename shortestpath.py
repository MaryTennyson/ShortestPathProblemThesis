import sys

class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
     
        
    def construct_graph(self, nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph) 

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
        
        return graph
    
    def get_nodes(self):
        return self.nodes

    def get_outgoing_edges_for_bf(self, node):
        return [(adjacent_node, value) for adjacent_node, value in self.graph.get(node, {}).items()]   

    def value(self, node1, node2):
        return self.graph[node1][node2]



def bellman_ford(graph, start_node, target_node):
    # Initialization
    distance = {node: float('inf') for node in graph.nodes}
    predecessor = {node: None for node in graph.nodes}
    distance[start_node] = 0

    # Relax edges repeatedly
    for _ in range(len(graph.nodes) - 1):
        for u in graph.nodes:
            for v, w in graph.get_outgoing_edges_for_bf(u):
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    predecessor[v] = u

    # Check for negative cycles
    for u in graph.nodes:
        for v, w in graph.get_outgoing_edges_for_bf(u):
            if distance[u] + w < distance[v]:
                raise ValueError("Graph contains negative weight cycle")

    # Reconstruct shortest path
    path = []
    node = target_node
    while node is not None:
        path.append(node)
        node = predecessor[node]

    path.reverse()
    return path, distance[target_node]


# The algorithm in action!
nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]
init_graph = {
    "Reykjavik": {"Oslo": 5, "London": 4},
    "Oslo": {"Reykjavik": 5, "Berlin": 1, "Moscow": 3},
    "Moscow": {"Oslo": 3, "Belgrade": 5, "Athens": 4},
    "London": {"Reykjavik": 4},
    "Rome": {"Berlin": 2, "Athens": 2},
    "Berlin": {"Rome": 2, "Oslo": 1},
    "Belgrade": {"Moscow": 5, "Athens": 1},
    "Athens": {"Rome": 2, "Moscow": 4, "Belgrade": 1}
}

graph = Graph(nodes, init_graph)


path, distance = bellman_ford(graph, "Reykjavik", "Rome")
print("BF /Shortest path from Reykjavik to Rome with a distance of {}: {}".format(distance, " -> ".join(path)))

# Find the shortest path from Reykjavik to Oslo
path, distance = bellman_ford(graph, "Reykjavik", "Moscow")
print("BF /Shortest path from Reykjavik to Oslo with a distance of {}: {}".format(distance, " -> ".join(path)))

# Find the shortest path from Reykjavik to Athens
path, distance = bellman_ford(graph, "Reykjavik", "Athens")
print("BF /Shortest path from Reykjavik to Athens with a distance of {}: {}".format(distance, " -> ".join(path)))