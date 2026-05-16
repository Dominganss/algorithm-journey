class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        new_nums = nums * 2 #优化 可以通过求模运算来节省内存。
        total = sum(nums)
        new_target = target % total
        k = target // total
        left = s = 0
        ans = inf
        n = len(nums)
        for i,x in enumerate(new_nums):
            s += x
            while s > new_target:
                s -= new_nums[left]
                left += 1
            if s == new_target:
                ans = min(ans,i - left + 1)
        return -1 if ans == inf else ans + k * n #未进入循环直接输出初始答案，因此可以在对变量进行初始赋值时，用一个答案永远不会出现的值。
            
            
