###给你一个字符串 s ，它只包含三种字符 a, b 和 c 。

#请你返回 a，b 和 c 都 至少 出现过一次的子字符串数目。
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = defaultdict(int)
        l = ans = 0
        for i,x in enumerate(s):
            cnt[x] += 1
            while len(cnt) == 3:
                cnt[s[l]] -= 1
                if cnt[s[l]] == 0:
                    del cnt[s[l]]
                l += 1
            ans += l
        return ans

#算法优化案例：
#基本思路：记录a,b,c最后一次出现的位置，窗口的左边界由三者中最小的位置决定。
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        pos = [-1,-1,-1]#记录a,b,c最后一次出现的位置
        ans = 0
        for i,x in enumerate(s):
            pos[ord(x) - 97] = i#ord()函数返回字符的ASCII码，a,b,c的ASCII码分别是97,98,99，因此ord(x) - 97可以将a,b,c映射到pos的索引0,1,2上
            left = min(pos)
            ans += left + 1#如果left == -1说明还没有遇到过满足条件的窗口，那么+1不会影响ans
        return ans
    
#错误案例：
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = ans = 0
        for i in range(len(s)):#bug:range()中的参数是int类型
            set_w = set(s[left : i + 1])
            if len(set_w) == 3:#bug:满足条件后再进入循环用于寻找长度最小的窗口
                while len(set_w) == 3:
                    left += 1
                    set_w = set(s[left : i + 1])
            ans += left ###bug:ans应该放在if语句的外部，非常微妙如果left == 0则说明没有遇到过满足的窗口，如果
                        ###left != 0则说明已经遇到过满足的窗口，即使目前的窗口不满足也会有，那么往右边界延申都是满足的。 
        return ans#优化：超时原因：set与切片的开销很大，滑动窗口的精髓是更新窗口只需更新增量，也就是在旧窗口下做加减法，而不是每次都重新计算整个窗口的状态。

"""@THOUGHTS
1. set与切片的开销很大，滑动窗口的精髓是更新窗口只需更新增量，也就是在旧窗口下做加减法，而不是每次都重新计算整个窗口的状态。
2. 由于题目要求a,b,c都至少出现一次，因此可以记录a,b,c最后一次出现的位置，窗口的左边界由三者中最小的位置决定。
"""