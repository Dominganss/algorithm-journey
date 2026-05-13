class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        new_nums = nums * 2
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
        return -1 if ans == inf else ans + k * n
            
            