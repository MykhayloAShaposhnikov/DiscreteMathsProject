'''Algorithms of finding distances between nodes in graph'''
from math import inf
from copy import deepcopy

def bellman_ford_algorithm(graph: 'nx.DiGraph', source):
    '''Bellman Ford algorithm'''
    list_of_ver = list(graph.nodes())
    list_of_edges = list(graph.edges())
    distance = {ver: float('inf') if ver != source else 0 for ver in list(graph.nodes())}
    predecessor = {ver: None for ver in list_of_ver}
    for i in range(1, len(list_of_ver)):
        for u, v in list_of_edges:
            new_value = distance[u] + graph.edges()[u, v]['weight']
            if distance[u] + graph.edges()[u, v]['weight'] < distance[v]:
                distance[v] = new_value
                predecessor[v] = u
    for u, v in list_of_edges:
        if distance[u] + graph.edges()[u, v]['weight'] < distance[v]:
            raise ValueError("Negative cycle detected")
    return predecessor, distance

def floyd_warshall_algorytm(graph: 'nx.Graph'):
    '''Floyd Warshall algorithm'''
    num_of_nodes = len(graph.nodes())
    list_of_edges = list(graph.edges())
    matrix_of_distances = {i: {j: graph.edges[i, j]['weight'] \
            if (i, j) in list_of_edges else 0 if i == j else inf for j in range(num_of_nodes)} \
            for i in range(num_of_nodes)}
    matrix_of_predecessors = {i: {j: i if i!=j else 0 for j in range(num_of_nodes)} \
            for i in range(num_of_nodes)}
    for k in range(0, num_of_nodes):
        matrix_k = deepcopy(matrix_of_distances)
        for i in range(num_of_nodes):
            for j in range(num_of_nodes):
                matrix_k[i][j] = min(matrix_of_distances[i][j], \
                            matrix_of_distances[i][k] + matrix_of_distances[k][j])
                if matrix_k[i][j] != matrix_of_distances[i][j]:
                    matrix_of_predecessors[i][j] = matrix_of_predecessors[k][j]
        matrix_of_distances = matrix_k
    if any(matrix_of_distances[n][n] < 0 for n in range(len(matrix_of_distances))):
        raise ValueError('Negative cycle detected')
    return matrix_of_predecessors, matrix_of_distances
