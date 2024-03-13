import networkx as nx
import numpy as np

class DirectedGraph: 
   
    def __init__(self): 
        
        self.numNodes = 0
        self.adjMatrix = [] 
        self.graph = nx.DiGraph()
    
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
        self.adjMatrix[a][b] = 1
        
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
    
    def toNetworkx(self):
        for i in range(self.numNodes):
            self.graph.add_node(i)
            
        for i in range(len(self.adjMatrix)):
            for j in range(len(self.adjMatrix[i])):
                if self.adjMatrix[i][j] == 1:
                    self.graph.add_edge(i, j)

        return self.graph