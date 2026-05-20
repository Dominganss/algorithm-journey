class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        left = n = 0
        cnt = defaultdict(int)
        for i,x in enumerate(nums):
            cnt[x] += 1
            n = max(n,cnt[x])
            if i - left + 1 - n > k:
                cnt[nums[left]] -= 1
                left += 1
        return  n

##优化案例：
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        left = max_cnt = 0
        cnt = [0] * (len(nums) + 1)
        for i,x in enumerate(nums):
            cnt[x] += 1
            max_cnt = max(max_cnt,cnt[x])
            if i - left + 1 - max_cnt > k:
                cnt[nums[left]] -= 1
                left += 1
        return max_cnt

"""@THOUGHTS
当元素值有明确且较小的上限时，直接分配一个长度为 len(nums) + 1 的静态数组来记录频率，
比使用 defaultdict(int) 的效率要高得多。数组的底层操作是基于连续内存地址的直接偏移计算，
省略了哈希函数的运算、哈希冲突的处理以及哈希表底层动态扩容的开销，这在数据量达到 $10^5$ 级别时，能够极其显著地降低常数时间。
"""