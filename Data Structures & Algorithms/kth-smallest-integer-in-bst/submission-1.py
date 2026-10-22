# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        count = 0

        def helper(node):
            if not node:
                return 0

            nonlocal res, count

            helper(node.left)
            count += 1
            if count == k:
                res = node.val
                return

            helper(node.right)

        helper(root)
        return res