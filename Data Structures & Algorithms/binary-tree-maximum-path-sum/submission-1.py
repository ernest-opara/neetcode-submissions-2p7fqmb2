# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float("-inf")

        def getMax(node):
            if not node:
                return 0

            nonlocal maxSum

            left = getMax(node.left)
            right = getMax(node.right)
            maxSum = max(maxSum, left + node.val + right)
            path = node.val + max(left, right)
            return max(0, path)

        getMax(root)

        return maxSum