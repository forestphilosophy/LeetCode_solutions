def word_split(phrase,list_of_words, output = None):
    
    if phrase == '':
        return []
    
    for i in range(len(phrase)):
        if phrase[:i+1] in list_of_words:
            output = phrase[:i+1]
            phrase = phrase.replace(phrase[:i+1],'')
            return [output] + word_split(phrase,list_of_words)
        
    return ['']
    
