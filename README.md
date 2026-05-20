# algorithm-journey
My Python algorithm practice log.
#  LeetCode Minimalist Log

> "Less is more." 专注核心逻辑与知识体系构建，拒绝无脑刷题。本项目使用 **Python 3** 记录我的算法精进之路。

---

##  Stats Tracker

每天进步一点点。手动更新，保持手感与专注。

- 🎯 **总计通过 (Total Solved):** `3`
- 🔥 **当前连续打卡 (Current Streak):** `3 Days`
- 🟢 **Easy:** `0` | 🟡 **Medium:** `3` | 🔴 **Hard:** `0`

---

##  核心心法 (Core Snippets)

*只记录最优雅、最硬核的算法模板。*

### 1. 单调非减滑动窗口 (求最大/最长)
求最长合法窗口时，抛弃 `while` 缩减，改为用 `if` 平移探测历史最大长度，完美实现 $O(N)$ 时间与极小常数。

```python
def sliding_window_max(nums: List[int], k: int) -> int:
    left = state = 0
    for right, x in enumerate(nums):
        state += x 
        # 不合法时只平移一格，长度永远保持历史最大，绝不缩水
        if state_is_invalid(state):
            state -= nums[left]
            left += 1
    return len(nums) - left

### 2. 利用while循环寻找临界窗口
利用while循环缩小左窗口来寻找从满足到不满足的临界情况，从而确定不同右指针下满足条件的最小窗口。例：1358 2799
while satisfied_the_condition:
    windows_state -= nums[left]
    left += 1