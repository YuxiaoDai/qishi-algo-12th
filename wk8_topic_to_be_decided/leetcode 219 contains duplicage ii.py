# 滑动窗口
#考虑数组 nums 中的每个长度不超过 k+1 的滑动窗口，同一个滑动窗口中的任意两个下标差的绝对值不超过 k。如果存在一个滑动窗口，其中有重复元素，则存在两个不同的下标 i 和 j 满足 nums[i]=nums[j]。如果所有滑动窗口中都没有重复元素，则不存在符合要求的下标。因此，只要遍历每个滑动窗口，判断滑动窗口中是否有重复元素即可。


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        s = set()

        for i, x in enumerate(nums):
            if i > k:
                s.remove(nums[i-k-1])
            if x in s:
                return True
            s.add(x)

        return False
