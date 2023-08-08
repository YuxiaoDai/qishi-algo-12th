class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
            return 0

        n = len(nums)
        fast = 1
        slow = 1
        while fast < n:
            if nums[fast] == nums[fast - 1]:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        return slow
