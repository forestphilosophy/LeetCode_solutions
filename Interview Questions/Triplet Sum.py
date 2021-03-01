def triplet_sum(l):
    arr_size = len(l)
    for i in range(0,arr_size-2):
        for j in range(i+1,arr_size-1):
            for k in range(j+1,arr_size):
                if l[i] + l[j] + l[k] == 0:
                    print (l[i],l[j],l[k])
