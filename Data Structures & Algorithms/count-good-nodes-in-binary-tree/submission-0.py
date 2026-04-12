# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def helper(node, maxSoFar):
            if not node:
                return 0
            
            nonlocal count

            if node.val >= maxSoFar:
                count += 1

            maxSoFar = max(maxSoFar, node.val)
            helper(node.left, maxSoFar)
            helper(node.right, maxSoFar)

        helper(root, float("-inf"))
        return count