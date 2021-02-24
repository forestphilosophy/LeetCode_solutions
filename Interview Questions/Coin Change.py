def rec_coin(target,coins):
    
    #Base case
    if target == 0:
        return 0
    
    if max(coins) > target:
        coins = [coin for coin in coins if coin < target]
    
    if max(coins) == 1:
        return target 
    
    return 1 + rec_coin(target-max(coins),coins)
