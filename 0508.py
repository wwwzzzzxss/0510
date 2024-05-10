import networkx as nx

def create_graph():
    G = nx.DiGraph()
    edges = [
        (1, 2), (2, 1),
        (2, 3), (3, 2),
        (3, 7), (7, 3),
        (4, 5), (5, 4),
        (5, 6), (6, 5),
        (6, 8), (8, 6),
        (11, 10), (12, 11),
        (12, 9),
        (1, 4), (4, 1),
        (2, 5), (5, 2),
        (3, 6),
        (7, 8),
        (4, 10), (10, 4),
        (11, 5),
        (6, 12), (12, 6),
        (8, 9), (9, 8)
    ]

    G.add_edges_from(edges)
    return G

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph.neighbors(start):
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def main():
    G = create_graph()
    start_node = 10
    end_nodes = [1, 7, 9]  # 多個終點
    all_paths = []
    for end_node in end_nodes:
        paths = find_all_paths(G, start_node, end_node)
        all_paths.extend(paths)


    print("All paths from node", start_node, "to nodes", end_nodes, "are:")
    for path in all_paths:
        print(path)

    
if __name__ == "__main__":
    main()
