from UnDirectedGraph import UnDirectedGraph
from DirectedGraph import DirectedGraph
import networkx as nx 
import matplotlib.pyplot as plt 
import os
  
def main():
    program_working = True
    graphChoose = True
    print("Witaj!")
    
    G = getFromFile()
    if isinstance(G, DirectedGraph) or isinstance(G, UnDirectedGraph):
        graphChoose = False
    
    while (graphChoose):
        print("Wybierz graf: (0 - skierowany, 1 nieskierowany)")
        try:
            grafWybor = int(input())
            if grafWybor == 0:
                G = DirectedGraph()
                graphChoose = False
            elif grafWybor == 1:
                G = UnDirectedGraph()
                graphChoose = False
            else:
                print("Podaj poprawny wybór!")
        except:
            print("Type a number!")
    
    while (program_working):
        print("""
                1. Dodaj krawędź
                2. Dodaj wierzchołek
                3. Usuń krawędź
                4. Usuń wierzchołek
                5. Wyznaczanie stopnia wierzchołka
                6. Wyznaczenie max i min stopnia grafu
                7. Wyznaczenie ile jest wierzchołków stopnia parzystego i nieparzystego
                8. Wypisanie ciągu stopni wierzchołków w grafie
                9. Wypisanie aktualnej macierzy sąsiedztwa
                10. Koniec
            """)
        try:
            wybor = int(input())
            match wybor:
                case 1: addEdge(G)
                case 2: addNode(G)
                case 3: removeEdge(G)
                case 4: removeNode(G)
                case 5: getNodeDegree(G)
                case 6: minMaxDegree(G)
                case 7: evenOddDegrees(G)
                case 8: sortedDegrees(G)
                case 9: printMatrix(G)
                case 10: 
                    visualize(G)
                    program_working = False
                case _: print("Type a correct number!")
        except:
            print("Type a number!")

def getFromFile():
    try:
        current_directory = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_directory, 'content.txt')
        file = open(file_path, "r")

        typeOfGraph = file.readline()

        if typeOfGraph == "skierowany\n":
            graph = DirectedGraph()
        elif typeOfGraph == "nieskierowany\n":
            graph = UnDirectedGraph()
        else:
           print("Wrong graph type!")
    
        numOfNodes = int(file.readline())

        for _ in range(numOfNodes):
            graph.addNode()

        lines = file.readline()
        while lines:
            nodes = lines.split(" ")
            if len(nodes) == 2:
                start = int(nodes[0])
                end = int(nodes[1])
                graph.addEdge(start, end)
            lines = file.readline()

        return graph
    except:
        print("Błąd przetwarzania pliku!")
        
def addEdge(g):
    print("Podaj pierwszą krawędź: ")
    startNode = int(input())
    print("Podaj drugą krawędź: ")
    endNode = int(input())
    
    numOfNodes = g.getNumOfNodes()
    
    if startNode < 0 or startNode >= numOfNodes or endNode < 0 or endNode >= numOfNodes:
        print("\nPodaj poprawne dane!\n")
    else:
        g.addEdge(startNode, endNode)
        print("\nKrawędź dodana!\n")

def addNode(g):
    g.addNode()
    print("\nWierzchołek dodany!\n")
    
def removeNode(g):
    print("Podaj wierzchołek: ")
    node = int(input())
    
    numOfNodes = g.getNumOfNodes()
    
    if node < 0 or node >= numOfNodes:
        print("\nPodaj poprawne dane!\n")
    else:
        g.removeNode(node)
        print("\nWierzchołek usunięty!\n")

def removeEdge(g):
    print("Podaj pierwszą krawędź: ")
    startNode = int(input())
    print("Podaj drugą krawędź: ")
    endNode = int(input())
    
    numOfNodes = g.getNumOfNodes()
    
    if startNode < 0 or startNode >= numOfNodes or endNode < 0 or endNode >= numOfNodes:
        print("\nPodaj poprawne dane!\n")
    else:
        g.removeEdge(startNode, endNode)
        print("\nKrawędź usunięta!\n")
    
def getNodeDegree(g):
    print("Podaj wierzchołek: ")
    node = int(input())
    
    numOfNodes = g.getNumOfNodes()
    
    if node < 0 or node >= numOfNodes:
        print("\nPodaj poprawne dane!\n")
    else:
        degree = g.getNodeDegree(node)
        print("\nStopień wierzchołka " + str(node) + " = " + str(degree) + "\n")

def minMaxDegree(g):
    minDegree, maxDegree = g.minMaxDegree()
    print("\nMin stopień grafu: " + str(minDegree) + "\nMax stopień grafu: " + str(maxDegree) + "\n")
    
def evenOddDegrees(g):
    evenCount, oddCount = g.countEvenOdd()
    print("\nParzystych wierzchołków: " + str(evenCount) + "\nNieparzystych wierzchołków: " + str(oddCount) + "\n")

def sortedDegrees(g):
    degreesSeq = g.getDegreesSeq()
    degreesAsString = " ".join(map(str, degreesSeq))
    print("\nPosortowany malejąco ciąg stopni w grafie: " + degreesAsString + "\n")
    
def printMatrix(g):
    matrix = g.getMatrix()
    for row in matrix:
        print(row)

def visualize(g):
    networkx = g.toNetworkx()
    pos = nx.spring_layout(networkx)
    nx.draw(networkx, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10, width=2.5)
    plt.title("Graf")
    plt.show()    
    
if __name__ == "__main__":
    main()