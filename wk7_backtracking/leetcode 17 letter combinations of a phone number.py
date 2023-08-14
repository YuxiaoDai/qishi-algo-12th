
class Solution:

    def __init__(self):
        self.result = []
        self.letters = ''
        self.dictionary = {'2': ['a','b', 'c'],
                      '3': ['d','e', 'f'],
                      '4': ['g','h', 'i'],
                      '5': ['j','k', 'l'],
                      '6': ['m','n', 'o'],
                      '7': ['p','q', 'r', 's'],
                      '8': ['t','u', 'v'],
                      '9': ['w','x', 'y', 'z']}
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return self.result
        
        def backtracking(digits, index):
            if index == len(digits):
                self.result.append(self.letters)
                return
            
            digit = digits[index]
            matching_letters = self.dictionary[digit]
            for i in range(len(matching_letters)):
                self.letters += matching_letters[i]
                #self.letters.append(matching_letters[i])
                backtracking(digits, index + 1)
                self.letters = self.letters[:-1]
                #self.letters.pop()
        
        backtracking(digits, 0)
        return self.result
            


