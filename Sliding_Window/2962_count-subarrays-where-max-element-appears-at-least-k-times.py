class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        s = max(nums)
        cnt = defaultdict(int)
        left = ans = 0
        for i,x in enumerate(nums):
            cnt[x] += 1
            while cnt[s] == k:
                cnt[nums[left]] -= 1
                left += 1
            ans += left
        return ans

"""THOUGHTS:
1. 由于这道题只关注最大值的个数，因此可以放弃对其他元素的统计，只需要关注
最大值的个数即可。因此可以放弃使用哈希表，值判断该位置上的值是否是最大值即可。
"""