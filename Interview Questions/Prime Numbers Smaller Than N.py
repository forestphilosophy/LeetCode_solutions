def prime_numbers(N):
    nums = list(range(2,N+1))
    boolean_list = [True]*(N-1)
    
    for num in nums:
        multiplier = 2
        while num * multiplier <= N:
            idx = nums.index(num * multiplier)
            boolean_list[idx] = False
            multiplier += 1
            
    primes_idx = [i for i, idx in enumerate(boolean_list) if idx == True]
    return [nums[i] for i in primes_idx]
