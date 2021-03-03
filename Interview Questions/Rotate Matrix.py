def rotate_90(matrix):
    
    m = len(matrix)
    n= len(matrix[0])
    
    #create a n*m matrix to store the results
    result = [ [0 for i in range(m)]] * n
    
    for i in range(n):
        result[i] = [x[i] for x in matrix][::-1]
        
    return result
