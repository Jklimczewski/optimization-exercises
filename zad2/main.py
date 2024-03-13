from UnDirectedGraph import UnDirectedGraph
from DirectedGraph import DirectedGraph
import os
  
def main():
    program_working = True
    print("Witaj!")
    
    G = getFromFile()
    if isinstance(G, DirectedGraph) or isinstance(G, UnDirectedGraph):
        print("\nPobrano graf!\n")
    else:
        G = pickGraphType()
    
    while (program_working):
        showMenu()
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
                case 10: isomorphismCheck(G)
                case 11:
                    visualize(G)
                    program_working = False
                case _: print("Podaj poprawną liczbę!")
        except:       
            print("Podaj liczbę!")
            
def showMenu():
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
                10. Sprawdzanie izomorfizmu
                11. Koniec
            """)
    
def pickGraphType():
    while (True):
        try:
            grafWybor = int(input("Wybierz graf: (0 - skierowany, 1 nieskierowany) "))
            if grafWybor == 0:
                G = DirectedGraph()
                return G
            elif grafWybor == 1:
                G = UnDirectedGraph()
                return G
            else:
                print("\nPodaj poprawny wybór!\n")
        except:
            print("\nWpisz liczbę!\n")
            
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
           raise("Zły typ grafu!")
    
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
        print("\nBłąd przetwarzania pliku!\n")
        
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

def isomorphismCheck(g):
    choosing = True
    while (choosing):
        try:
            wyborMetody = int(input("\nKtórą metodą: (0 - naiwna, 1 mnożenie macierzy) "))
            if wyborMetody == 0:
                isIsomorphic, i, j, k = g.containsC3Check()
                choosing = False
            elif wyborMetody == 1:
                isIsomorphic, i, j, k = g.containsC3CheckMultiply()
                choosing = False
            else:
                print("\nPodaj poprawny wybór!\n")
        except:
            print("\nWpisz liczbę!\n")
    if isIsomorphic:
        print(f"\nZnaleziono C3: {i} -> {j} -> {k}!\n")
    else:
        print("\nBrak  cyklu C3 lub graf nie jest prosty!\n")

def visualize(g):
    graph = g.toGraphviz()
    graph.view()
    
if __name__ == "__main__":
    main()