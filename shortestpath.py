class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

def floyd_warshall(graph, start_node, target_node):
    n = len(graph.nodes)
    dist = [[float('inf')] * n for _ in range(n)]
    pred = [[None] * n for _ in range(n)]

    for u, v, w in graph.edges:
        dist[u][v] = w
        pred[u][v] = u

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    path = []
    u = start_node
    while u != target_node:
        if pred[u][target_node] is None:
            return None, float('inf')  # There is no path
        path.append(u)
        u = pred[u][target_node]
    path.append(target_node)
    return path, dist[start_node][target_node]

# The algorithm in action!
nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]
edges = [
    ("Reykjavik", "Oslo", 5), ("Reykjavik", "London", 4),
    ("Oslo", "Reykjavik", 5), ("Oslo", "Berlin", 1), ("Oslo", "Moscow", 3),
    ("Moscow", "Oslo", 3), ("Moscow", "Belgrade", 5), ("Moscow", "Athens", 4),
    ("London", "Reykjavik", 4),
    ("Rome", "Berlin", 2), ("Rome", "Athens", 2),
    ("Berlin", "Rome", 2), ("Berlin", "Oslo", 1),
    ("Belgrade", "Moscow", 5), ("Belgrade", "Athens", 1),
    ("Athens", "Rome", 2), ("Athens", "Moscow", 4), ("Athens", "Belgrade", 1)
]

graph = Graph(nodes, edges)

# Find the shortest path from Reykjavik to Moscow
path, distance = floyd_warshall(graph, "Reykjavik", "Moscow")
if path:
    print("Shortest path from Reykjavik to Moscow with a distance of {}: {}".format(distance, " -> ".join(path)))
else:
    print("There is no path from Reykjavik to Moscow.")

# Find the shortest path from Reykjavik to Athens
path, distance = floyd_warshall(graph, "Reykjavik", "Athens")
if path:
    print("Shortest path from Reykjavik to Athens with a distance of {}: {}".format(distance, " -> ".join(path)))
else:
    print("There is no path from Reykjavik to Athens.")