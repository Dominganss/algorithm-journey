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