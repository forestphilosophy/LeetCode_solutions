def finder(arr1,arr2):
    
    count_arr1 = {}
    for i in arr1:
        if i not in count_arr1:
            count_arr1[i] = 1
        else:
            count_arr1[i] += 1
            
    count_arr2 = {}
    for i in arr2:
        if i not in count_arr2:
            count_arr2[i] = 1
        else:
            count_arr2[i] += 1
    
    try:
        difference = list(count_arr1.keys() - count_arr2.keys())[0]
        
    except:
        for key,val in count_arr1.items():
            if count_arr1[key] != count_arr2[key]:
                return key
            
    
    return difference
