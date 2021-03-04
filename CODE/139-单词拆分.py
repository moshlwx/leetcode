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
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''遍历s，匹配wordDict，若存在，则继续。打断后回退到上一层
        遍历wordDict，寻找s中的路径


        wordSet = set(wordDict)
        from queue import Queue 
        q = Queue()
        visted = set()

        q.put(wordDict[0])

        while not q.empty():
            q_size = q.qsize()

            for _ in range(qsize):
                cur = q.get()
            left += 1

        return True if 
        '''

        '''DFS多叉树遍历
        
        '''
        def backtrack(path, choose):
            '''
            输入路径、选择
            当len(path) == len(s) 成功
            '''
            if len(path) == len(s):
                return True

            if path in wordSet:
                backtrack(path, choose)
            else:
                return

            for c in choose:
                path.append(c)
                backtrack(path, choose)
                path.pop()

        res = False

        backtrack([], choose)

        return res
