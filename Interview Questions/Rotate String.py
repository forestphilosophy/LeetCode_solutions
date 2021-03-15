class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        list_of_letters = [i for i in A]
        
        if A == "" and B == "":
            return True
        if A == "" and B != "":
            return False
        
        for i in range(len(list_of_letters)):
            list_of_letters = list_of_letters[1:] + [list_of_letters[0]]
            new_word = ''.join(list_of_letters)
            if new_word == B:
                return True
        
        return False
