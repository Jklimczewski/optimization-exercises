import numpy as np

def strassen(x, y):
    def split(matrix):
        row, col = matrix.shape
        row2, col2 = row//2, col//2
        if row % 2 != 0:
            matrix = np.vstack((matrix, np.zeros((1, col))))
            row, _ = matrix.shape
        if col % 2 != 0:
            matrix = np.hstack((matrix, np.zeros((row, 1))))
            _, col = matrix.shape
        
        max_dim = max(row, col)
        if row < max_dim:
            matrix = np.vstack((matrix, np.zeros((max_dim - row, col))))
        if col < max_dim:
            matrix = np.hstack((matrix, np.zeros((row, max_dim - col))))
        
        return matrix[:max_dim//2, :max_dim//2], matrix[:max_dim//2, max_dim//2:], matrix[max_dim//2:, :max_dim//2], matrix[max_dim//2:, max_dim//2:]
    
    x, y = np.array(x), np.array(y)
    
    if len(x) == 1:
        return x * y
    a, b, c, d = split(x)
    e, f, g, h = split(y)
 
    p1 = strassen(a, f - h)  
    p2 = strassen(a + b, h)        
    p3 = strassen(c + d, e)        
    p4 = strassen(d, g - e)        
    p5 = strassen(a + d, e + h)        
    p6 = strassen(b - d, g + h)  
    p7 = strassen(a - c, e + f)  
 
    c11 = p5 + p4 - p2 + p6  
    c12 = p1 + p2           
    c21 = p3 + p4            
    c22 = p1 + p5 - p3 - p7  
    
    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22)))) 
    return c