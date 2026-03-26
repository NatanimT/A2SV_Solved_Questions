# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        def help(node):
            if not node:
                return 0
            left = help(node.left)
            right = help(node.right)
            self.moves += abs(left) + abs(right)
            return node.val + left + right - 1
        help(root)

        return self.moves
