def large_cont_sum(arr): 
    result = []
    for i in range(len(arr)):   
        steps = len(arr[i:])
        if i != len(arr)-1:
            l = [sum(arr[i:i+step]) for step in range(2,steps+1)]
            result.append(l)
        else:
            result.append([arr[-1]])
    
    return max([max(sublist) for sublist in result])
