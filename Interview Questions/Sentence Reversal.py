def rev_word(s):
    result = []
    words = s.split()
    words.reverse()
    for i in words:
        result.append(i)
    result = ' '.join(result)
    return result
