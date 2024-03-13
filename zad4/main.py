import os
import re


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def isGraphConnected(self):
        all_adges = []

        for row in self.graph:
            all_adges.append(row[0])
            all_adges.append(row[1])

        unique_edges = list(set(all_adges))

        if len(unique_edges) == self.V:
            return True
        else:
            return False

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x

        else:
            parent[y] = x
            rank[x] += 1

    def KruskalMST(self):
        if self.isGraphConnected():
            result = []
            i = 0
            e = 0

            self.graph = sorted(self.graph, key=lambda item: item[2])

            parent = []
            rank = []

            for node in range(self.V):
                parent.append(node)
                rank.append(0)

            while e < self.V - 1:
                u, v, w = self.graph[i]
                i = i + 1
                x = self.find(parent, u)
                y = self.find(parent, v)

                if x != y:
                    e = e + 1
                    result.append([u, v, w])
                    self.union(parent, rank, x, y)

            minimumCost = 0
            for u, v, weight in result:
                minimumCost += weight
                print(u, "--", v, "--", weight)
            print(minimumCost)

        else:
            print("graf niespójny - brak drzewa spinającego")


def main():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_directory, "content.txt")
    file = open(file_path, "r")

    tests = file.readline()
    first_line = []
    second_line = []
    graphs = []
    help_index = 0

    for _ in range(int(tests)):
        first_line.append(file.readline())
        second_line.append(file.readline())

    for string in first_line:
        pattern = r"n=(\d+)"
        match = re.search(pattern, string)

        if match:
            n_value = int(match.group(1))
            graphs.append(Graph(n_value))
        else:
            print("Bad text format")

    for graph in graphs:
        pattern2 = r"\{(\d+),(\d+)\}(\d+)"
        matches = re.findall(pattern2, second_line[help_index])

        for match in matches:
            number1, number2, number3 = match
            graph.addEdge(int(number1), int(number2), int(number3))

        graph.KruskalMST()
        help_index += 1


if __name__ == "__main__":
    main()
