'''
最大滑动窗口 vs 最小滑动窗口
最大滑动窗口模版
while j < len(nums):
    判断[i, j]是否满足条件
    while 不满足条件：
        i += 1 （最保守的压缩i，一旦满足条件了就退出压缩i的过程，使得滑窗尽可能的大）
    不断更新结果（注意在while外更新！）
    j += 1

最小滑动窗口模版
while j < len(nums):
    判断[i, j]是否满足条件
    while 满足条件：
        不断更新结果(注意在while内更新！)
        i += 1 （最大程度的压缩i，使得滑窗尽可能的小）
    j += 1
https://leetcode.cn/problems/fruit-into-baskets/solutions/1437444/shen-du-jie-xi-zhe-dao-ti-he-by-linzeyin-6crr/
'''
from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        i, j = 0, 0
        fruit_class_count = 0
        fruit_map = defaultdict(int)
        result = 0

        while j < len(fruits):

            # fruit_map里面添加fruit[j]
            fruit_map[fruits[j]] += 1
            # 如果fruit[j]是新水果，添加fruit_class_count加1
            if fruit_map[fruits[j]] == 1:
                fruit_class_count += 1

            while fruit_class_count > 2:
                fruit_map[fruits[i]]-= 1
                if fruit_map[fruits[i]] == 0:
                    fruit_class_count -= 1
                i += 1
            
            j += 1

            result = max(result, j - i)
        
        return result
            