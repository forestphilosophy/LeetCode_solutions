import numpy as np

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        matrix = np.array(matrix)
        
        m = len(matrix)
        n = len(matrix[0])
        
        for k in range(-m+1, n):

            diag = np.diag(matrix, k=k)
            
            if len(list(set(diag))) > 1:
                return False
            
        return True
