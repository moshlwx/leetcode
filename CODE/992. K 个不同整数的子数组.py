'''
992. K 个不同整数的子数组
给定一个正整数数组 A，如果 A 的某个子数组中不同整数的个数恰好为 K，则称 A 的这个连续、不一定不同的子数组为好子数组。

（例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。）

返回 A 中好子数组的数目。

 

示例 1：

输入：A = [1,2,1,2,3], K = 2
输出：7
解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
示例 2：

输入：A = [1,2,1,3,4], K = 3
输出：3
解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].
 

提示：

1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length
'''


class Solution:
    def minsubarrays(self, nums, k: int) -> int: 
        # 返回不同整数个数至多为K的子数组个数
        left = 0
        right = 0
        diff_cnt = 0
        res = 0

        from collections import Counter
        window = Counter()

        while right < len(nums):
            c = nums[right]
            right += 1
            window[c] += 1

            if window[c] == 1:
                diff_cnt += 1

            while diff_cnt > k:
                d = nums[left]
                left += 1
                window[d] -= 1

                if window[d] == 0:
                    diff_cnt -= 1

            # 迭代结束时，[left, right)区间包含最多K个不同字符。
            # 包含K个不同字符的序列中，不超过K个字符的子串个数恰好等于区间长度。
            # [1,2,3,2]包含3个不同字符，则包含不超过3个不同字符最多子串个数为4
            res += right - left
        return res


    def subarraysWithKDistinct(self, A, K: int) -> int:
        '''问题转换为最多K个不同整数组成的子数组，func(K) - func(K-1)即为恰好K个不同整数的解
        '''
        return self.minsubarrays(A, K) - self.minsubarrays(A, K-1)


# 输入：
A = [1, 2, 1, 2, 3]
K = 2
# 输出：7
# 解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
print(Solution().subarraysWithKDistinct(A, K))

# 输入：
A = [1, 2, 1, 3, 4]
K = 3
# 输出：3
# 解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].
print(Solution().subarraysWithKDistinct(A, K))
