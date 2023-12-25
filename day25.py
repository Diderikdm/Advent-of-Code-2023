import networkx as nx

with open("day25.txt", "r") as file:
    graph = nx.Graph()
    for row in file.read().splitlines():
        left, right = row.split(': ')
        for other in right.split(' '):
            graph.add_edge(left, other)
    bisected = nx.spectral_bisection(graph)
    print(len(bisected[0]) * len(bisected[1]))