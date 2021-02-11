def pair_sum(arr,k):
    ans = 0
    cursor = 0
    for i in arr:
        cursor += 1 
        for j in range(cursor,len(arr)):
            try:
                if i + arr[j] == k:
                    ans += 1
            except:
                continue
    return ans
