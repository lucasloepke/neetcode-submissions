# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth):
            furthest = depth + 1
            if node:
                left = node.left
                right = node.right
                if left:
                    furthest = max(furthest, dfs(left, depth+1))
                if right:
                    furthest = max(furthest, dfs(right, depth+1))
            else:
                return depth
            return max(depth, furthest)
        return dfs(root, 0)