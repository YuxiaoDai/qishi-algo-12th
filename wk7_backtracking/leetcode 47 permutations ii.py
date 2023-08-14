#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.result = []
        self.path = []

    def backtracking(self, nums, used_list):
        if len(self.path) == len(nums):
            self.result.append(self.path[:])
            return
        for i in range(len(nums)):

            # used[i - 1] == true，说明同一树枝nums[i - 1]使用过
            # used[i - 1] == false，说明同一树层nums[i - 1]使用过
            # 如果同一树层nums[i - 1]使用过则直接跳过

            if used_list[i] == True:
                continue
            if i > 0 and nums[i] == nums[i-1] and used_list[i-1] == False:
                continue
            used_list[i] = True
            self.path.append(nums[i])
            self.backtracking(nums, used_list)
            self.path.pop()
            used_list[i] = False

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used_list = [False] * len(nums)
        nums = sorted(nums)
        self.backtracking(nums, used_list)
        return self.result
# @lc code=end

