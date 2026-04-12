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
            nonlocal pre

            if l > r:
                return None

            nodeVal = preorder[pre]
            node = TreeNode(nodeVal)
            pre += 1

            mid = inorderMap[nodeVal]

            node.left = helper(l, mid - 1)
            node.right = helper(mid + 1, r)

            return node
        return helper(0, len(inorder) - 1)