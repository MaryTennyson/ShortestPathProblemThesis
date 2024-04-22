class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        """
        This method makes sure that the graph is symmetrical. In other words,
        if there's a path from node A to B with a value V, there needs to be a
        path from node B to node A with a value V.
        """
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
        "Returns the nodes of the graph."
        return self.nodes

    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]


   
    def bellman_ford(self, start_node):
        # Step 1: Initialize distances from start_node to all other nodes as INFINITY
        distance = {node: float('inf') for node in self.nodes}
        distance[start_node] = 0
        
        # Step 2: Relax all edges |V| - 1 times
        for _ in range(len(self.nodes) - 1):
            for node in self.nodes:
                for neighbor in self.get_outgoing_edges(node):
                    if distance[node] + self.value(node, neighbor) < distance[neighbor]:
                        distance[neighbor] = distance[node] + self.value(node, neighbor)
        
        # Step 3: Check for negative-weight cycles
        for node in self.nodes:
            for neighbor in self.get_outgoing_edges(node):
                if distance[node] + self.value(node, neighbor) < distance[neighbor]:
                    raise ValueError("Graph contains a negative-weight cycle")
        
        return distance


# Driver's code
if __name__ == '__main__':
 nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]

init_graph = {}
for node in nodes:
 init_graph[node] = {}

init_graph["Reykjavik"]["Oslo"] = 5
init_graph["Reykjavik"]["London"] = 4
init_graph["Oslo"]["Berlin"] = 1
init_graph["Oslo"]["Moscow"] = 3
init_graph["Moscow"]["Belgrade"] = 5
init_graph["Moscow"]["Athens"] = 4
init_graph["Athens"]["Belgrade"] = 1
init_graph["Rome"]["Berlin"] = 2
init_graph["Rome"]["Athens"] = 2

# We now use this values to create an object of the Graph class
graph = Graph(nodes, init_graph)

    # function call
shortest_path= graph.bellman_ford(start_node="Rome")

print(shortest_path)