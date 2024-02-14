'''Our implelentation of algoruthms of finding minimum spanning tree'''


#Our implementation of Kruskal algorithm
def find_set(node, sets, s_edges_i):
    '''Find set of nodes'''
    for j, jth in enumerate(sets):
        if s_edges_i[node] in sets[j]:
            return jth

def kruskal_algorithm(graph):
    '''Main Kruskal algorithm function'''
    sum_of_weights = 0
    edges = list(graph.edges(data=True))
    s_edges = sorted(edges, key= lambda x : x[2]['weight'])
    sets = [set([x]) for x in range(len(graph.nodes))]
    res = []
    for i, ith in enumerate(s_edges):
        u = find_set(0, sets, s_edges[i])
        v = find_set(1, sets, s_edges[i])
        if u != v:
            res.append(ith[:2])
            sum_of_weights += ith[2]['weight']
            sets[sets.index(u)] = u.union(v)
            sets.remove(v)
    return res, sum_of_weights

#Our implementation of Prima algorithm
def prima_algoritm(graph: 'nx.Graph') -> tuple[list[tuple], int]:
    '''Our implementation of Prima algorithm'''
    spanning_tree = []
    sum_of_weights = 0
    list_of_nodes = list(graph.nodes)
    start = list_of_nodes[0]
    seen = set([start])
    list_of_nodes.remove(start)
    while list_of_nodes:
        lst = []
        for node in seen:
            for neighbour in graph.adj[node]:
                if neighbour not in seen:
                    lst.append((node, neighbour, graph.edges[node, neighbour]['weight']))
        node1, node2, weight = min(lst, key = lambda x: x[2])
        spanning_tree.append((node1, node2))
        seen.add(node2)
        sum_of_weights += weight
        list_of_nodes.remove(node2)
    return spanning_tree, sum_of_weights
