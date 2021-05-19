r'''
剑指 Offer 32 - III. 从上到下打印二叉树 III
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]
 

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
        '''二叉树层次遍历，增加sign实现之字形
        '''
        if not root:
            return []

        from queue import Queue
        q = Queue()

        q.put(root)
        res = []
        sign = 1

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
            res.append(res_cur[::sign])
            sign *= -1

        return res
