r'''
111. 二叉树的最小深度
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。

 

示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：2
示例 2：

输入：root = [2,null,3,null,4,null,5,null,6]
输出：5
 

提示：

树中节点数的范围在 [0, 105] 内
-1000 <= Node.val <= 1000
'''
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        '''层次遍历，遇到叶子节点即结束返回当前深度
        '''
        if not root:
            return 0

        from queue import Queue
        q = Queue()
        q.put(root)
        min_depth = 1

        while not q.empty():
            q_size = q.qsize()

            for _ in range(q_size):
                cur = q.get()
                # print(cur.right, cur.left)
                if not cur.right and not cur.left:
                    return min_depth

                for n in [cur.left, cur.right]:
                    if n:
                        q.put(n)

            min_depth += 1

        return -1
