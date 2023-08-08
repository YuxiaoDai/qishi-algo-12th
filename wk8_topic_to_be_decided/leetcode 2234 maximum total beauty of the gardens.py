class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        flowers.sort()
        n = len(flowers)
        if flowers[0] >= target:  # 剪枝，此时所有花园都是完善的
            return n * full

        leftFlowers = newFlowers - target * n  # 填充后缀后，剩余可以种植的花
        for i in range(n):
            flowers[i] = min(flowers[i], target)  # 去掉多余的花
            leftFlowers += flowers[i]  # 补上已有的花

        ans, x, sumFlowers = 0, 0, 0
        for i in range(n + 1):  # 枚举后缀长度 n-i
            if leftFlowers >= 0:
                # 计算最长前缀的长度
                while x < i and flowers[x] * x - sumFlowers <= leftFlowers:
                    sumFlowers += flowers[x]
                    x += 1  # 注意 x 只增不减，二重循环的时间复杂度为 O(n)
                beauty = (n - i) * full  # 计算总美丽值
                if x:
                    beauty += min((leftFlowers + sumFlowers) // x, target - 1) * partial
                ans = max(ans, beauty)
            if i < n:
                leftFlowers += target - flowers[i]
        return ans
