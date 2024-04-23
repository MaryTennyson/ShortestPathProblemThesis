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

    def get_outgoing_edges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        return self.graph[node1][node2]

def dijkstra_algorithm(graph, start_node, target_node):
    unvisited_nodes = list(graph.get_nodes())
    shortest_path = {}
    previous_nodes = {}
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    shortest_path[start_node] = 0

    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
        
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node
        
        unvisited_nodes.remove(current_min_node)
        if current_min_node == target_node:
            break
        
    if shortest_path[target_node] == max_value:
        print("There is no path from {} to {}.".format(start_node, target_node))
    else:
        path = []
        node = target_node
        while node != start_node:
            path.append(node)
            node = previous_nodes[node]
        path.append(start_node)
        print("DJ  /Shortest path from {} to {} with a distance of {}:".format(start_node, target_node, shortest_path[target_node]))
        print(" -> ".join(reversed(path)))





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

# Find the shortest path from Reykjavik to Rome
dijkstra_algorithm(graph, "Reykjavik", "Rome")

# Find the shortest path from Reykjavik to Oslo
dijkstra_algorithm(graph, "Reykjavik", "Moscow")

# Find the shortest path from Reykjavik to Athens
dijkstra_algorithm(graph, "Reykjavik", "Athens")
