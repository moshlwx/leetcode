'''
剑指 Offer II 018. 有效的回文
给定一个字符串 s ，验证 s 是否是 回文串 ，只考虑字母和数字字符，可以忽略字母的大小写。

本题中，将空字符串定义为有效的 回文串 。

 

示例 1:

输入: s = "A man, a plan, a canal: Panama"
输出: true
解释："amanaplanacanalpanama" 是回文串
示例 2:

输入: s = "race a car"
输出: false
解释："raceacar" 不是回文串
 

提示：

1 <= s.length <= 2 * 105
字符串 s 由 ASCII 字符组成
 

注意：本题与主站 125 题相同： https://leetcode-cn.com/problems/valid-palindrome/
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True

        # 双指针，头尾开始检查
        left = 0
        right = len(s)-1

        while left <= right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum() and left < right:
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1

        return True


s = "   "
# true
print(Solution().isPalindrome(s))


s = "race a car"
# false
print(Solution().isPalindrome(s))


s = "A man, a plan, a canal: Panama"
# true
print(Solution().isPalindrome(s))