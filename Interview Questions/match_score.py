def diff(arr):
    
    first_score = 0
    second_score = 0
    
    whose_turn = 1
    
    while not len(arr) == 0:
        score = arr.pop(0)
        
        if whose_turn == 1: # player 1's turn
            first_score += score
            if score % 2 == 0: # even number => reverse arr
                arr.reverse()
            else: # odd number => do nothing
                pass
            whose_turn = 2
        
        else: # player 2's turn
            second_score += score
            if score % 2 == 0: # even number => reverse arr
                arr.reverse()
            else: # odd number => do nothing
                pass
            whose_turn = 1            
            
    return (first_score - second_score)   
            
