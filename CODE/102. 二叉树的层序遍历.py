r'''
102. 二叉树的层序遍历
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

 

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
'''
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []

        from queue import Queue
        q = Queue()

        q.put(root)
        res = []

        while not q.empty():
            q_size = q.qsize()
            res_cur = []

            for _ in range(q_size):
                cur = q.get()
                # 每层的记录在先序做，后序会需要较多的空值处理
                res_cur.append(cur.val)

                for n in [cur.left, cur.right]:
                    if n:
                        q.put(n)
                        
            # 层次遍历完
            res.append(res_cur)

        return res
