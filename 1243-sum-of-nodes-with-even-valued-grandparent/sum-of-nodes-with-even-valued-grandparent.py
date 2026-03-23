# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        ans =[0]
        def help(node, ans):
            if not node:
                return 
            if node.val % 2==0:
                if node.left and node.left.left:
                    ans[0] += node.left.left.val
                if node.left and node.left.right:
                    ans[0] += node.left.right.val
                if node.right and node.right.right:
                    ans[0] += node.right.right.val
                if node.right and node.right.left:
                    ans[0] += node.right.left.val

            help(node.left, ans)
            help(node.right, ans)
        help(root, ans)
        return ans[0]
