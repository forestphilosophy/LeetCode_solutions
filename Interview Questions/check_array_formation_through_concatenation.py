class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:

        arr_str = 'dummy,' + ','.join([str(i) for i in arr]) + ','
 
        for piece in pieces:
            
            if len(piece) == 1:
                
                piece_str = ',' + str(piece[0]) + ','
                
            else:
                piece_str = ',' + ','.join([str(i) for i in piece]) + ','
            
     
            if piece_str not in arr_str:
                return False

        return True
                        
