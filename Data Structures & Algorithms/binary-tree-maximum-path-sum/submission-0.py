# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        
        def getMax(node):
            nonlocal max_sum
            if not node:
                return 0

            left = getMax(node.left)
            right = getMax(node.right)
            max_sum = max(max_sum, node.val + left + right)
            path = node.val + max(left, right)
            return max(0, path)

        getMax(root)
        return max_sum