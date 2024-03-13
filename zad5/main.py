import os
from graphviz import Digraph


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.graphical = Digraph()

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, src):
        dist = [float("Inf")] * self.V
        path = {v: [] for v in range(self.V)}
        dist[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    path[v] = path[u] + [v]

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graf zawiera ujemny cykl")
                return

        self.print_solution(dist, path)

    def print_solution(self, dist, path):
        print("Wierzchołek \t Odległość od v \t Przebyta droga")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}\t\t\t{path[i]}")

    def toGraphviz(self):
        for i in range(self.V):
            self.graphical.node(str(i))

        for row in self.graph:
            self.graphical.edge(str(row[0]), str(row[1]), label=str(row[2]))
        return self.graphical


def getFromFile():
    try:
        current_directory = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_directory, "content.txt")
        file = open(file_path, "r")

        numOfNodes = int(file.readline())
        g = Graph(numOfNodes)

        lines = file.readline()
        while lines:
            nodes = lines.split(" ")
            if len(nodes) == 3:
                start = int(nodes[0])
                end = int(nodes[1])
                weight = int(nodes[2])
                g.add_edge(start, end, weight)
            lines = file.readline()

        return g
    except:
        raise Exception("Błąd przetwarzania pliku!")


def main():
    g = getFromFile()

    g.bellman_ford(0)

    visual = g.toGraphviz()
    visual.view()


if __name__ == "__main__":
    main()
