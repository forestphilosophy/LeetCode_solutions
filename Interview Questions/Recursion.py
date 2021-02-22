def sum_func(n):
    num_of_digits = len(str(n))
    if num_of_digits == 1:
        return n
    
    result = int(str(n)[0])
    div = 10 ** (num_of_digits-1)
    n = n % div
    
    return result + sum_func(n) 
