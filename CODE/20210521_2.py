# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bisect_tree_path(self, root: TreeNode) -> int:
        self.visited = set()
        self.res_sum = 0

        def dfs(root, path):
            if not root:
                return
            if not root.left and not root.right:

                path_sum = sum([p.val for p in path])

                cur_sum = 0
                node_minus = None

                for _, p in enumerate(path):
                    if path_sum - p.val == cur_sum*2:
                        node_minus = p
                        break
                    cur_sum += p.val
                if node_minus \
                        and node_minus not in self.visited:
                    self.res_sum -= node_minus.val
                    self.visited.add(node_minus)

            path.append(root.left)
            dfs(root.left, path)
            path.pop()

            self.res_sum += root.val

            path.append(root.right)
            dfs(root.right, path)
            path.pop()

        dfs(root, [root])

        return self.res_sum
