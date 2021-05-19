r'''
剑指 Offer 32 - I. 从上到下打印二叉树
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]
 

提示：

节点总数 <= 1000
'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []

        from queue import Queue
        q = Queue()
        res = []

        q.put(root)

        while not q.empty():
            q_size = q.qsize()

            for _ in range(q_size):
                cur = q.get()
                res.append(cur.val)

                for n in [cur.left, cur.right]:
                    if n:
                        q.put(n)

        return res
