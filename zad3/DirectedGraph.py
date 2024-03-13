import numpy as np
from strassen import strassen
from graphviz import Digraph

class DirectedGraph: 
   
    def __init__(self): 
        
        self.numNodes = 0
        self.adjMatrix = [] 
        self.graph = Digraph()
    
    def getNumOfNodes(self):
        return self.numNodes
    
    def getMatrix(self):
        return self.adjMatrix
        
    def addNode(self):
        if self.numNodes == 0:
            self.adjMatrix.append([0])
        else:
            for row in self.adjMatrix:
                row.append(0)
            self.adjMatrix.append(list(np.zeros(len(self.adjMatrix[0]), int)))
          
        self.numNodes += 1
        
    def addEdge(self, a, b):
        self.adjMatrix[a][b] += 1
        
    def removeEdge(self, a, b):
        self.adjMatrix[a][b] = 0
        
    def removeNode(self, x):
        self.numNodes -= 1
        del self.adjMatrix[x]
        
        for row in self.adjMatrix:
            del row[x]
        
    def getNodeDegree(self, x):
        posDegree = 0
        for i in range(self.numNodes):
            posDegree += self.adjMatrix[i][x]
        negDegree = sum(self.adjMatrix[x])

        return posDegree, negDegree
    
    def minMaxDegree(self):
        if self.numNodes == 0:
            return None, None
        
        minDegree = self.getNodeDegree(0)[0] + self.getNodeDegree(0)[1]
        maxDegree = 0 

        for i in range(self.numNodes):
            posDegree, negDegree = self.getNodeDegree(i)
            totalDegree = posDegree + negDegree
            if totalDegree < minDegree:
                minDegree = totalDegree
            if totalDegree > maxDegree:
                maxDegree = totalDegree

        return minDegree, maxDegree

    def countEvenOdd(self):
        even_count = 0
        odd_count = 0

        for i in range(self.numNodes):
            posDegree, negDegree = self.getNodeDegree(i)
            totalDegree = posDegree + negDegree
            if totalDegree % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        return even_count, odd_count
    
    def getDegreesSeq(self):
        degreesSeq = [(self.getNodeDegree(i)[1] +self.getNodeDegree(i)[0]) for i in range(self.numNodes)]
        degreesSeq.sort(reverse=True)
        
        return degreesSeq

    def isGraphSimple(self):
        for i in range(len(self.adjMatrix)):
            if self.adjMatrix[i][i] != 0:
                return False

        for i in range(len(self.adjMatrix)):
            for j in range(len(self.adjMatrix[i])):
                if self.adjMatrix[i][j] > 1 or (self.adjMatrix[i][j] == 1 and self.adjMatrix[j][i] == 1):
                    return False

        return True
    
    def containsC3Check(self):
        if self.numNodes < 3 or self.isGraphSimple() == False:
            return False, None, None, None

        for v1 in range(self.numNodes):
            for v2 in range(v1 + 1, self.numNodes):
                for v3 in range(v2 + 1, self.numNodes):
                    if self.adjMatrix[v1][v2] > 0 and self.adjMatrix[v2][v3] > 0 and self.adjMatrix[v3][v1] > 0:
                        return True, v1, v2, v3
        return False, None, None, None
    
    def containsC3CheckMultiply(self):
        if self.numNodes < 3 or self.isGraphSimple() == False:
            return False, None, None, None
        
        square = strassen(self.adjMatrix, self.adjMatrix)
        np.fill_diagonal(square, 0)
        for i in range(self.numNodes):
            for j in range(self.numNodes):
                if square[i][j] > 0 and self.adjMatrix[j][i] > 0:
                    for k in range(self.numNodes):
                        if self.adjMatrix[i][k] > 0 and self.adjMatrix[k][j] > 0:
                            return True, i, k, j
        return False, None, None, None   
    
    def toGraphviz(self):
        for i in range(self.numNodes):
            self.graph.node(str(i))
            
        for i in range(self.numNodes):
            for j in range(self.numNodes):
                for _ in range(self.adjMatrix[i][j]):
                        self.graph.edge(str(i), str(j))
        return self.graph