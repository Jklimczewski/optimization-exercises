import numpy as np
from strassen import strassen
from graphviz import Graph

class UnDirectedGraph: 
   
    def __init__(self): 
        
        self.numNodes = 0
        self.adjMatrix = [] 
        self.graph = Graph()
    
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
        if a == b:
            self.adjMatrix[a][b] += 2
        else:
            self.adjMatrix[a][b] += 1
            self.adjMatrix[b][a] += 1
        
    def removeEdge(self, a, b):
        self.adjMatrix[a][b] = 0
        self.adjMatrix[b][a] = 0

    def removeNode(self, x):
        self.numNodes -= 1
        del self.adjMatrix[x]
        
        for row in self.adjMatrix:
            del row[x]
        
    def getNodeDegree(self, x):
        degree = sum(self.adjMatrix[x])
        return degree 
    
    def minMaxDegree(self):
        if self.numNodes == 0:
            return None, None

        minDegree = self.getNodeDegree(0)
        maxDegree = 0 

        for i in range(self.numNodes):
            degree = self.getNodeDegree(i)
            if degree < minDegree:
                minDegree = degree
            if degree > maxDegree:
                maxDegree = degree

        return minDegree, maxDegree

    def countEvenOdd(self):
        even_count = 0
        odd_count = 0

        for i in range(self.numNodes):
            degree = self.getNodeDegree(i)
            if degree % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        return even_count, odd_count
    
    
    def getDegreesSeq(self):
        degreesSeq = [self.getNodeDegree(i) for i in range(self.numNodes)]
        degreesSeq.sort(reverse=True)
        
        return degreesSeq
    
    def isGraphSimple(self):
        for i in range(len(self.adjMatrix)):
            if self.adjMatrix[i][i] != 0:
                return False

        for i in range(len(self.adjMatrix)):
            for j in range(len(self.adjMatrix[i])):
                if self.adjMatrix[i][j] > 1:
                    return False

        return True
    
    def containsC3Check(self):
        if self.numNodes < 3 or self.isGraphSimple() == False:
            return False, None, None, None
    
        for i in range(self.numNodes):
            for j in range(i+1, self.numNodes):
                if self.adjMatrix[i][j] != 0:
                    for k in range(j+1, self.numNodes):
                        if self.adjMatrix[i][k] != 0 and self.adjMatrix[j][k] != 0:
                            return True, i , j, k
        return False, None, None, None
    
    def containsC3CheckMultiply(self):
        if self.numNodes < 3 or self.isGraphSimple() == False:
            return False, None, None, None
        
        square = strassen(self.adjMatrix, self.adjMatrix)
        np.fill_diagonal(square, 0)
        for i in range(self.numNodes):
            for j in range(self.numNodes):
                if square[i][j] > 0 and self.adjMatrix[i][j] > 0:
                    for k in range(self.numNodes):
                        if self.adjMatrix[i][k] > 0 and self.adjMatrix[j][k] > 0:
                            return True, i, j, k
        return False, None, None, None    
                    
    def toGraphviz(self):
        for i in range(self.numNodes):
            self.graph.node(str(i))
            
        for i in range(self.numNodes):
            for j in range(i, self.numNodes):
                if self.adjMatrix[i][j] > 0 and i != j:
                    for _ in range(self.adjMatrix[i][j]):
                            self.graph.edge(str(i), str(j))
                elif self.adjMatrix[i][j] > 0 and i == j:
                    for _ in range(int(self.adjMatrix[i][j]/2)):
                        self.graph.edge(str(i), str(j))
        return self.graph