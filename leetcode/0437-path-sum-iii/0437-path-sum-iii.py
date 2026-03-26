# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        freq = {0:1}
        def help(node,curr_sum):
            if not node:
                return 0
            curr_sum += node.val
            count = freq.get(curr_sum - targetSum, 0)
            freq[curr_sum] = freq.get(curr_sum, 0) + 1
            count += help(node.left, curr_sum)
            count += help(node.right, curr_sum)
            freq[curr_sum] -= 1
            return count

        return help(root, 0)


        