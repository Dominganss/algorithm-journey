class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        left = ans1 =  ans2 = total1 = total2 = 0
        n = len(nums)
        for i in range(n):
            total1 += nums[i]
            while total1 >= goal and left <= i:#bug:在case2中，不加left <= i会导致left一直向右收缩。
                total1 -= nums[left]
                left += 1
            ans1 += left
        left = 0
        for j in range(n):
            total2 += nums[j]
            while total2 >= goal + 1:
                total2 -= nums[left]
                left += 1
            ans2 += left
        return ans1 - ans2
    
"""@THOUGHTS:
在计数问题中，直接求“精确等于某个条件”的集合往往极其困难，因为它缺乏单调性。
但如果我们把条件放宽，求“小于等于某个条件”的集合，往往具备严格的单调性，极其容易计算。
因此我们可以通过求“小于等于goal”的子数组数目减去“小于等于goal-1”的子数组数目来得到“等于goal”的子数组数目。
这其实是差分思想：$F(\text{恰好等于 } K) = F(\text{最多等于 } K) - F(\text{最多等于 } K-1)$
"""