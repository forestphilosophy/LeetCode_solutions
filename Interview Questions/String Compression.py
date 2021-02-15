def compress(s):
    
    if not s:
        print ('')
    
    result = {}
    for i in s:
        if i not in result:
            result[i] = 1
        else:
            result[i] += 1
            
    ans = ''
    for k,v in result.items():
        ans = ans + k + str(v)
        
    return ans 
