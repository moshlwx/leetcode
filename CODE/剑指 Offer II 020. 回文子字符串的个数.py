'''
剑指 Offer II 020. 回文子字符串的个数
给定一个字符串 s ，请计算这个字符串中有多少个回文子字符串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

 

示例 1：

输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"
示例 2：

输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
 

提示：

1 <= s.length <= 1000
s 由小写英文字母组成
 

注意：本题与主站 647 题相同：https://leetcode-cn.com/problems/palindromic-substrings/ 
'''


class Solution:
    def countSubstrings(self, s: str) -> int:
        '''暴力解法，全排列，每个子串判断是否回文
        需要考虑做剪枝，循环中已经判断为回文的可以跳过判断
        从中间扩散，判断回文子串。
        mid width只能找到奇数的回文串。偶数的判断需要考虑
        '''
        cnt = 0
        for mid in range(0, 2*len(s)):
            width = 0
            left = round(mid/2 - width)
            right = round(mid/2 + width)

            while left >= 0 and right < len(s) and left <= right:

                print(s[left: right+1])
                if s[left] == s[right]:
                    cnt += 1
                    left -= 1
                    right += 1
                else:
                    break
        return cnt

    def countSubstrings_baoli(self, s: str) -> int:
        '''暴力解法，全排列，每个子串判断是否回文
        O(n^3)
        '''
        def isPlainText(sub_s):
            left = 0
            right = len(sub_s)-1

            while left <= right:
                if sub_s[left] != sub_s[right]:
                    return False
                left += 1
                right -= 1
            return True

        cnt = 0
        # 字符串的所有子串
        for start in range(len(s)):
            for end in range(start+1, len(s)+1):
                # print(s[start: end])
                if isPlainText(s[start: end]):
                    cnt += 1
        return cnt


s = "abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
print(Solution().countSubstrings(s))

s = "aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
print(Solution().countSubstrings(s))
