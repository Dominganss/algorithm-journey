class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(set(nums))#set:无序不重复元素集
        cnt = defaultdict(int)
        left = ans = 0
        for i,x in enumerate(nums):
            cnt[x] += 1
            while len(cnt) == n:
                l = nums[left]
                cnt[l] -= 1
                if cnt[l] == 0:
                    del cnt[l]
                left += 1
            ans += left #left:左边界，i:右边界，left之前的子数组都满足条件
        return ans

"""@THOUGHTS
1. 统计数组中不同元素的个数n,可以使用set来实现。
2. 利用while循环来寻找恰好包含n个不同元素的长度最小子数组，使用一个字典来统计当前窗口中每个元素的出现次数。
在这个过程中，如果当前窗口包含了n个不同元素，就尝试缩小窗口的左边界，直到窗口中不再包含n个不同元素为止。并且
每次满足条件时，统计以当前右边界为结尾的子数组数量，即left之前的子数组都满足条件。
总而言之，就是利用while循环来寻找处在满足条件与不满足条件之间的边界，并统计满足条件的子数组数量。
"""