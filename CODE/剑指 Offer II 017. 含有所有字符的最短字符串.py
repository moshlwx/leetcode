'''
剑指 Offer II 017. 含有所有字符的最短字符串
给定两个字符串 s 和 t 。返回 s 中包含 t 的所有字符的最短子字符串。如果 s 中不存在符合条件的子字符串，则返回空字符串 "" 。

如果 s 中存在多个符合条件的子字符串，返回任意一个。

 

注意： 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。

 

示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC" 
解释：最短子字符串 "BANC" 包含了字符串 t 的所有字符 'A'、'B'、'C'
示例 2：

输入：s = "a", t = "a"
输出："a"
示例 3：

输入：s = "a", t = "aa"
输出：""
解释：t 中两个字符 'a' 均应包含在 s 的子串中，因此没有符合条件的子字符串，返回空字符串。
 

提示：

1 <= s.length, t.length <= 105
s 和 t 由英文字母组成
 

进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？

 

注意：本题与主站 76 题相似（本题答案不唯一）：https://leetcode-cn.com/problems/minimum-window-substring/
'''


import time


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''滑动窗口
        遍历S，统计窗口符合t的所有情况，保存最小窗口
        # valid_len可以省去，复用window_current中大于0的元素个数counter.elements()当count被设置为0，会忽略，
        但是获取iterator的长度需要遍历迭代，每次判断复杂度太高
        '''
        from collections import Counter

        left = 0
        right = 0
        window_target = Counter(t)
        window_current = Counter()
        # window_target_set = set(t)
        valid_len = 0
        res = s*2

        while right < len(s):
            c = s[right]
            right += 1

            window_current[c] += 1
            if window_current[c] == window_target[c]:
                valid_len += 1

            # 循环结束时应当是左边界追上右边界，或者窗口跳出最小满足条件
            while valid_len == len(window_target):
                if right-left <= len(res):
                    res = s[left: right]

                d = s[left]
                left += 1
                window_current[d] -= 1
                if window_current[d] == window_target[d]-1:
                    valid_len -= 1

        # return res
        return res if len(res) <= len(s) else ""

st = time.perf_counter()

s = "ADOBECODEBANC"
t = "ABCC"
# 输出："BANC"
# 解释：最短子字符串 "BANC" 包含了字符串 t 的所有字符 'A'、'B'、'C'
print(Solution().minWindow(s, t))

s = "ADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCC"
t = "ABCCADOBECODEBANCADOBECODEBADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCADOBECODEBANCANCADOBECODEBANC"
# 输出："BANC"
# 解释：最短子字符串 "BANC" 包含了字符串 t 的所有字符 'A'、'B'、'C'
print(Solution().minWindow(s, t))

s = "a"
t = "a"
# 输出："BANC"
# 解释：最短子字符串 "BANC" 包含了字符串 t 的所有字符 'A'、'B'、'C'
print(Solution().minWindow(s, t))

print(time.perf_counter() - st)
