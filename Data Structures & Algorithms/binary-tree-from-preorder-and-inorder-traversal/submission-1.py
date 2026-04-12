# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {val: i for i, val in enumerate(inorder)}
        pre = 0
        
        def helper(l,r):
            if l > r:
                return None
            nonlocal pre

            rootVal = preorder[pre]
            pre += 1
            root = TreeNode(rootVal)
            mid = inorderMap[rootVal]
            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)
            return root

        return helper(0, len(inorder) - 1)