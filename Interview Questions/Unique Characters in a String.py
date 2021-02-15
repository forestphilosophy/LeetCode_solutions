def uni_char(s):
    result = {}
    
    if not s:
        return True
    
    for i in s:
        if i not in result:
            result[i] = 1
        else:
            result[i] += 1
    
    if max(list(result.values())) > 1:
        return False
    else:
        return True
