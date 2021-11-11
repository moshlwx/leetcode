'''
剑指 Offer II 005. 单词长度的最大乘积
给定一个字符串数组 words，请计算当两个字符串 words[i] 和 words[j] 不包含相同字符时，它们长度的乘积的最大值。
假设字符串中只包含英语的小写字母。如果没有不包含相同字符的一对字符串，返回 0。

示例 1:

输入: words = ["abcw","baz","foo","bar","fxyz","abcdef"]
输出: 16 
解释: 这两个单词为 "abcw", "fxyz"。它们不包含相同字符，且长度的乘积最大。
示例 2:

输入: words = ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4 
解释: 这两个单词为 "ab", "cd"。
示例 3:

输入: words = ["a","aa","aaa","aaaa"]
输出: 0 
解释: 不存在这样的两个单词。
 

提示：

2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] 仅包含小写字母
 

注意：本题与主站 318 题相同：https://leetcode-cn.com/problems/maximum-product-of-word-lengths/
'''


class Solution:
    def maxProduct(self, words) -> int:
        '''二进制思路
        26个字母对应26位长度的二进制数字，1表示含对应字母
        位运算的一些trick可以快速计算是否重合
        '''
        res = [0]*len(words)

        for i in range(len(words)):
            for c in words[i]:
                res[i] |= 1 << ord(c) - ord('a')

        return max_res

    def maxProduct_counter(self, words) -> int:
        # 每个元素做Counter
        # for word in words 若不重合则计算长度乘积
        # 空间利用可以优化，Counter可以在循环中计算
        # O(N^2*26^2)
        from collections import Counter
        words_count = [Counter(word) for word in words]
        max_res = 0

        for i in range(len(words_count)):
            for j in range(i, len(words_count)):
                if len(words_count[i].keys() & words_count[j].keys()) == 0:
                    max_res = max(max_res, len(words[i])*len(words[j]))

        return max_res


# 输入:
words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
# 输出: 4

print(Solution().maxProduct(words))
