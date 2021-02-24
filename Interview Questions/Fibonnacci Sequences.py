#Recursive method
def fib_rec(n):
    
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    
    return fib_rec(n-1) + fib_rec(n-2)
    
#Iterative method
def fib_iter(n):
    
    l = [i for i in range(n+1)]
    
    for i in range(n+1):
        
        if i == 0 or i == 1:
            continue
        else:    
            l[i] = l[i-1] + l[i-2]
            
    return l[n]

#Dynamic programming
n = 10
cache = [None] * (n + 1)


def fib_dyn(n):
    
    #Base Case
    if n == 0 or n == 1:
        return n

    #check Cache
    if cache[n] != None:
        return cache[n]
    
    #Keep Settingg Cache
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
    
    return cache[n]
