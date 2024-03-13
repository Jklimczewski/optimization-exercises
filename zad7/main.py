import networkx as nx
import random
import matplotlib.pyplot as plt


def minimal_spanning_tree(G):
    t = nx.minimum_spanning_tree(G, "weight", "kruskal")
    return t


def find_odd_vertices(T):
    o = [v for v, d in T.degree() if d % 2 != 0]
    return o


def perfect_matching(O_subgraph):
    m = nx.min_weight_matching(O_subgraph, weight="weight")
    return m


def create_multigraph(T, M, o_subgraph):
    h = nx.MultiGraph(T)
    for u, v in M:
        edge = o_subgraph.get_edge_data(u, v)
        h.add_edge(u, v, weight=edge["weight"])
    return h


def eulerian_cycle(H):
    eulerian_circuit = list(nx.eulerian_circuit(H))
    return eulerian_circuit


def hamilton_cycle(eulerian_circuit):
    visited = set()
    visited.add(eulerian_circuit[0][0])
    hamilton_cycle = [eulerian_circuit[0][0]]

    for edge in eulerian_circuit:
        if edge[1] not in visited:
            hamilton_cycle.append(edge[1])
            visited.add(edge[1])

    hamilton_cycle.append(eulerian_circuit[0][0])
    return hamilton_cycle


def visualize(G, hamilton_circuit=None):
    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, width=4)

    if hamilton_circuit:
        hamiltonian_edges = [
            (hamilton_circuit[i], hamilton_circuit[i + 1])
            for i in range(len(hamilton_circuit) - 1)
        ]

        hamilton_length = 0
        for u, v in hamiltonian_edges:
            hamilton_length += G.get_edge_data(u, v)["weight"]
        print(hamilton_length)

        nx.draw_networkx_edges(
            G, pos, edgelist=hamiltonian_edges, edge_color="red", width=2
        )

    nx.draw_networkx_labels(G, pos, font_size=20)
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    plt.axis("off")
    plt.tight_layout()
    plt.show()


def check_triangle_inequality(G):
    for u, v in G.edges():
        for x in G.neighbors(v):
            if x != u:
                if not G.has_edge(u, x):
                    continue
                if G[u][v]["weight"] + G[v][x]["weight"] < G[u][x]["weight"]:
                    return False
    return True


def main():
    G = nx.complete_graph(5)
    for u, v in G.edges():
        G.edges[u, v]["weight"] = random.randint(1, 10)

    check_triangle = check_triangle_inequality(G)
    while check_triangle == False:
        for u, v in G.edges():
            G.edges[u, v]["weight"] = random.randint(1, 10)
        check_triangle = check_triangle_inequality(G)

    visualize(G)

    # Krok 1
    t = minimal_spanning_tree(G)
    visualize(t)

    # Krok 2
    o = find_odd_vertices(t)
    o_subgraph = G.subgraph(o)
    visualize(o_subgraph)

    # Krok 3
    m = perfect_matching(o_subgraph)

    # Krok 4
    h = create_multigraph(t, m, o_subgraph)

    # Krok 5
    eulerian_circuit = eulerian_cycle(h)
    print("Cykl Eulera:", eulerian_circuit)
    hamilton_circuit = hamilton_cycle(eulerian_circuit)
    print("Cykl Hamiltona:", hamilton_circuit)

    visualize(G, hamilton_circuit)


if __name__ == "__main__":
    main()
