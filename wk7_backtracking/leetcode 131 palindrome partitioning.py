#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:

    def __init__(self) -> None:
        self.result = []
        self.path = []

    def isPalindrome(self, x: str):
        i = 0
        j = len(x) - 1
        while i <= j:
            if x[i] != x[j]:
                return False
            i += 1
            j -= 1
        return True

    def backtracking(self, string, startIndex):
        if startIndex == len(string):
            self.result.append(self.path[:])
            return

        for i in range(startIndex, len(string)):
            subString = string[startIndex: i + 1]
            if self.isPalindrome(subString):
                self.path.append(subString)
                self.backtracking(string, i + 1)
                self.path.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.backtracking(s, 0)
        return self.result

# @lc code=end

