'''
139. 单词拆分
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
'''


class Solution:
    def wordBreak_dfs(self, s: str, wordDict) -> bool:
        wordSet = set(wordDict)

        # visited用数组或者set按照下标访问，用字典复杂度会超
        visted = [-1 for _ in range(len(s))]

        def can_break(start):
            if start == len(s):
                return True
            if visted[start] != -1:
                return visted[start]

            for i in range(start+1, len(s)+1):
                prefix = s[start: i]
                if prefix in wordSet and can_break(i):
                    visted[start] = True
                    return True
            visted[start] = False
            return False

        return can_break(0)

    def wordBreak_bfs(self, s: str, wordDict) -> bool:
        from queue import Queue

        wordSet = set(wordDict)
        q = Queue()
        q.put(0)
        visted = set()

        while not q.empty():
            cur = q.get()
            if cur in visted:
                continue
            visted.add(cur)

            for i in range(cur+1, len(s)+1):
                prefix = s[cur: i]

                if prefix in wordSet:
                    # 子串在wordSet中，若i未到边界，继续判断cur_start到i的子串
                    if i < len(s):
                        q.put(i)
                    # 若i到边界，返回真
                    else:
                        return True

        return False

    def wordBreak(self, s: str, wordDict) -> bool:
        '''动态规划
        dp[i][j] 前j个字符串是否满足
        状态转移：dp[i][j] = dp[i-1][j-1] and item[j: j+1] in wordSet or dp[i-1][j-k] and item[j-k: j+1] in wordSet
        '''
        wordSet = set(wordDict)
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True

        for j in range(1, len(s)+1):
            for k in range(j, 0, -1):
                dp[j] = dp[j] or (dp[j-k] and s[j-k: j] in wordSet)
            
        return dp[-1]


s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa",
            "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
s = "leetcode"
wordDict = ["leet", "code"]

print(Solution().wordBreak(s, wordDict))
