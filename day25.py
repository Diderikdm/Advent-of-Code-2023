import networkx as nx

with open("day25.txt", "r") as file:
    graph = nx.Graph()
    for row in file.read().splitlines():
        left, right = row.split(': ')
        for other in right.split(' '):
            graph.add_edge(left, other)
    cc = nx.spectral_bisection(graph)
    print(len(cc[0]) * len(cc[1]))