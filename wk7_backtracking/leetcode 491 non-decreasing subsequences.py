#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#

# @lc code=start
from ast import Num


class Solution:

    def __init__(self) -> None:
        self.result = []
        self.path = []

    def backtracking(self, nums, startIndex):
        if len(self.path) >= 2:
            self.result.append(self.path[:])

        if startIndex >= len(nums):
            return
        
        for i in range(startIndex, len(nums)):
            if i > startIndex and nums[i] in nums[startIndex: i]:
                continue
            if self.path and nums[i] < self.path[-1]:
                continue
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(nums, 0)
        return self.result


# @lc code=end

