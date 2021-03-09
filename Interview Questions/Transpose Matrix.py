class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        m = len(matrix)
        n = len(matrix[0])
        
        #create a n*m matrix
        result = [[0 for i in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                result[i][j] = matrix[j][i]
            
        return result 
