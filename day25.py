from networkx import Graph, spectral_bisection

with open("day25.txt", "r") as file:
    graph = Graph()
    for row in file.read().splitlines():
        node, others = row.split(': ')
        for other in others.split(' '):
            graph.add_edge(node, other)
    bisected = spectral_bisection(graph)
    print(len(bisected[0]) * len(bisected[1]))