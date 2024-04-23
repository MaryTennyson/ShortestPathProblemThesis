import sys
from timeit import default_timer as timer

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
nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens", "Paris", "Madrid",
         "Lisbon", "Dublin", "Brussels", "Vienna", "Stockholm", "Warsaw", "Budapest", "Prague", "Zurich", "Copenhagen"]

init_graph = {
    "Reykjavik": {"Oslo": 5, "London": 4, "Berlin": 8},
    "Oslo": {"Reykjavik": 5, "Moscow": 7, "Stockholm": 2},
    "Moscow": {"Oslo": 7, "Berlin": 6, "Vienna": 10},
    "London": {"Reykjavik": 4, "Paris": 3, "Madrid": 7},
    "Rome": {"Berlin": 3, "Athens": 5, "Paris": 8},
    "Berlin": {"Reykjavik": 8, "Moscow": 6, "Rome": 3},
    "Belgrade": {"Athens": 3, "Warsaw": 4, "Budapest": 2},
    "Athens": {"Rome": 5, "Belgrade": 3, "Madrid": 9},
    "Paris": {"London": 3, "Rome": 8, "Madrid": 5},
    "Madrid": {"London": 7, "Athens": 9, "Paris": 5},
    "Lisbon": {"Dublin": 6, "Paris": 10, "Madrid": 11},
    "Dublin": {"Lisbon": 6, "London": 9, "Paris": 8},
    "Brussels": {"London": 4, "Paris": 5, "Berlin": 7},
    "Vienna": {"Berlin": 4, "Prague": 3, "Warsaw": 6},
    "Stockholm": {"Oslo": 2,"Copenhagen": 5},
    "Warsaw": {"Vienna": 6, "Berlin": 5, "Budapest": 4},
    "Budapest": {"Belgrade": 2, "Warsaw": 4, "Prague": 3},
    "Prague": {"Vienna": 3, "Budapest": 3, "Zurich": 7},
    "Zurich": {"Prague": 7, "Vienna": 8, "Paris": 10},
    "Copenhagen": {"Stockholm": 5, "Berlin": 5}
}


graph = Graph(nodes, init_graph)

t0=timer()
path, distance = bellman_ford(graph, "Reykjavik", "Vienna")
t1=timer()

print(t1-t0)

print("BF /Shortest path from Reykjavik to Copenhagen with a distance of {}: {}".format(distance, " -> ".join(path)))
t0=timer()
# Find the shortest path from Reykjavik to Oslo
path, distance = bellman_ford(graph, "Reykjavik", "Stockholm")
t1=timer()
print(t1-t0)
print("BF /Shortest path from Reykjavik to Stockholm with a distance of {}: {}".format(distance, " -> ".join(path)))
