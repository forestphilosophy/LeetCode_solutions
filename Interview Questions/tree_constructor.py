def tree_constructor(str_arr):
    parents = {}
    children = {}
    
    for _str in str_arr:
        a,b = map(int, _str.replace('(', '').replace(')', '').split(','))

        if a in children:
          children[a] += 1
          if children[a] > 2:
            return False
          
        else:
          children[a] = 1
          
        if b in parents:
          parents[b] += 1
          if parents[b] > 2:
            return False
            
        else:
          parents[b] = 1  
          
    return True
    

