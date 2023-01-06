def is_prime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if (n%i) == 0:
            return False
        
    return True

min_pen_l = []
og_arr = [1,3,4,6,6,7]

get_prime = True
def alt_primes(arr,get_prime=False):

    if len(arr) == 0:
        return 0
    
    for idx,num in enumerate(arr): 
        if get_prime:
            if not any(is_prime(num) for num in arr):
                min_pen_l.append(sum(arr))
                continue
            else:
                if is_prime(num):
                    min_pen_l.append(alt_primes(arr[:idx]+arr[idx+1:],get_prime=False))
                else:
                    continue
                    
        elif not get_prime:
            if all(is_prime(num) for num in arr):
                min_pen_l.append(sum(arr))
                continue  
            else:
                if is_prime(num):
                    continue
                else:
                    min_pen_l.append(alt_primes(arr[:idx]+arr[idx+1:],get_prime=True))

    return min(min_pen_l)

min(alt_primes(og_arr,True),alt_primes(og_arr,False))
