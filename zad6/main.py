from itertools import combinations
import igraph as ig
import os
import graphviz


class Graph:
    def __init__(self, vertices):
        self.graph = ig.Graph()
        self.graph.add_vertices(vertices)
        self.graphical = graphviz.Graph()
        self.vertices = vertices

    def add_adge(self, x, y, weight):
        self.graph.add_edge(x, y, weight=weight)

    def hierholzer_algorithm_circuit(self):
        temp_graph = self.graph.copy()

        start_vertex = 0
        for v in self.graph.vs:
            if v.degree() > 0:
                start_vertex = v.index
                break

        stack = [start_vertex]
        circuit = []

        while len(stack) > 0:
            v = stack[-1]

            neighbors = temp_graph.neighbors(v)
            if len(neighbors) > 0:
                u = neighbors[0]
                stack.append(u)
                temp_graph.delete_edges((v, u))
            else:
                circuit.append(stack.pop())

        return circuit[::-1]

    def hierholzer_algorithm_path(self, u, v):
        temp_graph = self.graph.copy()
        stack = [u]
        path = []

        while len(stack) > 0:
            current_vertex = stack[-1]

            if len(temp_graph.neighbors(current_vertex)) > 0:
                next_vertex = temp_graph.neighbors(current_vertex)[0]
                stack.append(next_vertex)
                temp_graph.delete_edges(temp_graph.get_eid(current_vertex, next_vertex))
            else:
                path.append(stack.pop())

        if path[0] != v:
            return None

        return path[::-1]

    # Przypadek 1: Graf G jest eulerowski
    def eulerian_graph(self):
        if not self.graph.is_connected():
            return None
        for v in self.graph.vs:
            if v.degree() % 2 != 0:
                return None

        return self.hierholzer_algorithm_circuit()

    # Przypadek 2: Graf G jest półeulerowski
    def semi_eulerian_graph(self):
        if not self.graph.is_connected():
            return None

        odd_vertices = [v for v in self.graph.vs if v.degree() % 2 != 0]
        if len(odd_vertices) != 2:
            return None

        euler_path = self.hierholzer_algorithm_path(
            odd_vertices[0].index, odd_vertices[1].index
        )
        print("Ścieżka Eulera:", euler_path)

        shortest_path = self.graph.get_shortest_paths(
            odd_vertices[0], odd_vertices[1], weights="weight"
        )[0]
        print("Najkrótsza ścieżka:", shortest_path)

        return euler_path + shortest_path[:-1][::-1]

    # Przypadek 3: Rozwiązanie dla grafu z wierzchołkami nieparzystego stopnia
    def chinese_postman(self):
        odd_vertices = [v.index for v in self.graph.vs if v.degree() % 2 != 0]

        g_prime = ig.Graph.Full(len(odd_vertices))
        shortest_paths = self.graph.distances(
            source=odd_vertices, target=odd_vertices, weights="weight"
        )

        for i, j in combinations(range(len(odd_vertices)), 2):
            weight = shortest_paths[i][j]
            g_prime.add_edge(i, j, weight=weight)

        print(g_prime)
        return

    def toGraphviz(self):
        return self.graphical


def getFromFile():
    try:
        current_directory = os.path.dirname(os.path.realpath(__file__))
        file = input("Podaj plik: ")
        file_path = os.path.join(current_directory, file)
        file = open(file_path, "r")

        numOfNodes = int(file.readline())
        g = Graph(numOfNodes)
        for i in range(numOfNodes):
            g.graphical.node(str(i))

        lines = file.readline()
        while lines:
            nodes = lines.split(" ")
            if len(nodes) == 3:
                start = int(nodes[0])
                end = int(nodes[1])
                weight = int(nodes[2])
                g.add_adge(start, end, weight)
                g.graphical.edge(str(start), str(end), label=str(weight))
            lines = file.readline()
        return g
    except:
        raise Exception("Błąd przetwarzania pliku!")


def main():
    g = getFromFile()
    visual = g.toGraphviz()
    visual.view()

    eulerian_circuit = g.eulerian_graph()
    if eulerian_circuit:
        print("Rozwiązanie - Cykl Eulera:", eulerian_circuit)
        exit(0)

    eulerian_path = g.semi_eulerian_graph()
    if eulerian_path:
        print("Rozwiązanie:", eulerian_path)
        exit(0)

    chinese_postman_result = g.chinese_postman()
    print("Nowy graf eulerowski:", chinese_postman_result)


if __name__ == "__main__":
    main()
