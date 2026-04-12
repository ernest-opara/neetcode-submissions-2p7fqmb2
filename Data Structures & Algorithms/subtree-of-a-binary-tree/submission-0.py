# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def helper(root, subroot):
            if not root and not subroot:
                return True
            
            if root and subroot and root.val == subroot.val:
                return helper(root.left,subroot.left) and helper(root.right, subroot.right)
            return False

        if not subRoot:
            return True
        
        if not root:
            return False

        if helper(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)