####给你一个整数数组 nums 和一个 正整数 k 。请你统计有多少满足 「 nums 中的 最大 元素」至少出现 k
#  次的子数组，并返回满足这一条件的子数组的数目。子数组是数组中的一个连续元素序列。
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


#代码优化
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        s = max(nums)
        left = ans = cnt = 0
        for i,x in enumerate(nums):
            if x == s :
                cnt += 1
            while cnt == k:
                if nums[left] == s:
                    cnt -= 1
                left += 1
            ans += left 
        return ans

"""@THOUGHTS
1. 由于这道题只关注最大值的个数，因此可以放弃对其他元素的统计，只需要关注
最大值的个数即可。因此可以放弃使用哈希表，值判断该位置上的值是否是最大值即可。
"""