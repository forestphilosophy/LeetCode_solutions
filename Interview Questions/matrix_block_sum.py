class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        res = []
        
        i = 0
        
        for row in range(len(mat)):
            j = 0
            sub_list = []
            
            for col in range(len(mat[0])):
                r_min = (i - k) if (i - k) > 0 else 0
                c_min = (j - k) if (j - k) > 0 else 0
                
                r_max = min(i+k,len(mat))
                c_max = min(j+k,len(mat[0]))
                
                relevant_mat = mat[r_min:r_max+1]
                sub_list.append(sum([sum(l[c_min:c_max+1]) for l in relevant_mat]))
                j += 1   
                
            res.append(sub_list)
            i += 1
            
        return res
