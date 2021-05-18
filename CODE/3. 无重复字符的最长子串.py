'''
3. 无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0
 

提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''滑动窗口问题
        '''
        from collections import Counter

        left = 0
        right = 0
        window = Counter()
        max_len = 0

        while right < len(s):
            # 暂存待入窗口值，滑动右边界
            c = s[right]
            right += 1
            window[c] += 1

            while window[c] > 1:
                # 若c为重复值，移动左边界直到无重复
                d = s[left]
                left += 1
                window[d] -= 1

            # 退出循环时，表示窗口内无重复值，满足条件，更新结果
            max_len = max(max_len, right - left)

        return max_len


s = "bbbbb"
print(Solution().lengthOfLongestSubstring(s))
