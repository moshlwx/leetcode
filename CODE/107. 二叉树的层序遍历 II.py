r'''
107. 二叉树的层序遍历 II
给定一个二叉树，返回其节点值自底向上的层序遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层序遍历为：

[
  [15,7],
  [9,20],
  [3]
]
'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        if not root:
            return []

        from queue import Queue

        q = Queue()
        q.put(root)
        res = []

        while not q.empty():
            q_size = q.qsize()
            row = []

            for _ in range(q_size):
                cur = q.get()
                row.append(cur.val)

                for n in [cur.left, cur.right]:
                    if n:
                        q.put(n)

            # 倒序遍历，每层遍历结果插入到序列最前
            res.append(row)

        return res[::-1]
