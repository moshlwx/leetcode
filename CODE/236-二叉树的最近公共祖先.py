'''
236. 二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

 

示例 1：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
示例 2：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
示例 3：

输入：root = [1,2], p = 1, q = 2
输出：1
 

提示：

树中节点数目在范围 [2, 105] 内。
-109 <= Node.val <= 109
所有 Node.val 互不相同 。
p != q
p 和 q 均存在于给定的二叉树中。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''递归需要思考的问题
        1. 返回值：若pq为root的子节点，返回节点为最近公共祖先；若root中只含p or q返回节点；若pq均不在root中，返回空值
        2. 输入：pq不变，root递归传入左右子树
        3. 得到递归结果的处理：比较左右子树返回值，对应第一点要求返回对应值
        '''

        # base case
        if not root:
            return None

        if root == p or root==q:
            return root

        left_ans = self.lowestCommonAncestor(root.left, p, q)
        right_ans = self.lowestCommonAncestor(root.right, p, q)

        # 若左右迭代均不为空，说明情况1or2则root是最近公共祖先
        if left_ans and right_ans:
            return root

        # 若两者均为空，说明情况3，返回空值
        if not left_ans and not right_ans:
            return None

        # 其余情况为仅一个非空，返回非空的那个
        return left_ans if left_ans else right_ans