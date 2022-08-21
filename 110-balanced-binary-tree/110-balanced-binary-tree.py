# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         return self.dfs(root)
        
        
#     def dfs(self, root: Optional[TreeNode]):
#         if root is None:
#             return [True, 0]
#         left, right = self.dfs(root.left), self.dfs(root.right)
#         balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
#         return [balanced, 1 + max(left[1], right[1])]
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root) != -1
    
    def dfs(self, root: Optional[TreeNode]):
        if root is None:
            return 0
        left, right = self.dfs(root.left), self.dfs(root.right)
        if left == -1 or right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1
        
            