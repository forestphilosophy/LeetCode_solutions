def anagram(s1,s2):
    temp1 = {}
    temp2 = {}
    
    for i in [char for char in s1 if char != ' ']:
        if i in temp1:
            temp1[i] += 1
        else:
            temp1[i] = 1
    
    for i in [char for char in s2 if char != ' ']:
        if i in temp2:
            temp2[i] += 1
        else:
            temp2[i] = 1
    
    if temp1 == temp2:
        return True
    
    else:
        return False
