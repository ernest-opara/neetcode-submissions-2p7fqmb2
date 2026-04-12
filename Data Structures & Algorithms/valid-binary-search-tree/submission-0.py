# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(low, node, high):
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return validate(low, node.left, node.val) and validate(node.val, node.right, high)

        return validate(-math.inf, root, math.inf)