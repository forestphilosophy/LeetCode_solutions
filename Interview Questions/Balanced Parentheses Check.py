def balance_check(s):
    
    square_brackets = round_brackets = curly_brackets = []
    
    for i in s:
        if i == '[' or i == ']':
            square_brackets.append(i)
            
        elif i == '(' or i == ')':
            round_brackets.append(i)
        
        elif i == '{' or i == '}':
            curly_brackets.append(i)
            
    return (square_brackets.count('[') == square_brackets.count(']')) & (round_brackets.count('(') == round_brackets.count(')')) & (curly_brackets.count('{') == curly_brackets.count('}'))
