'''
剑指 Offer II 002. 二进制加法
给定两个 01 字符串 a 和 b ，请计算它们的和，并以二进制字符串的形式输出。

输入为 非空 字符串且只包含数字 1 和 0。

 

示例 1:

输入: a = "11", b = "10"
输出: "101"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
 

提示：

每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。
 

注意：本题与主站 67 题相同：https://leetcode-cn.com/problems/add-binary/
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''按位处理字符串 O(N)复杂度
        '''

        carry = 0
        cur_a = 0
        cur_b = 0
        res = ''

        len_a = len(a)
        len_b = len(b)

        max_len = max(len_a, len_b)
        a_with_0 = ('0'*max_len + a)[-max_len:]
        b_with_0 = ('0'*max_len + b)[-max_len:]

        for i in range(max_len-1, -1, -1):
            cur = (int(a_with_0[i]) + int(b_with_0[i]) + carry) % 2
            carry = (int(a_with_0[i]) + int(b_with_0[i]) + carry) > 1
            res = str(cur) + res

        if carry == 1:
            res = '1' + res

        return res


a = '10001111011'
b = '1001'

print(Solution().addBinary(a, b))
