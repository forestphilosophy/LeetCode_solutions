def Sort_duplicates(l):
    hash_table = {}
    pos = 0
    result = []

    for i in l:
        if i not in hash_table:
            hash_table[i] = pos
            pos += 1

        else:
            continue

    for val,pos in hash_table.items():
        result += [val]*l.count(val)
    
    return result 
