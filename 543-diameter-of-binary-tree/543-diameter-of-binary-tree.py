# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0]
        
        def dfs(root):
            if root is None:
                return -1
            hleft = dfs(root.left)
            hright = dfs(root.right)
            result[0] = max(result[0], hleft + hright + 2)
            return 1 + max(hleft, hright)
        
        dfs(root)
        return result[0]