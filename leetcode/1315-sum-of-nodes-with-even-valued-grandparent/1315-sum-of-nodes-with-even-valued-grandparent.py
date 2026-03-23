# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([(root, -1, -1)])
        val = 0
        while q:
            node, parent, grandP = q.popleft()
            if grandP % 2 == 0:
                val += node.val 
            if node.left:
                q.append([node.left, node.val, parent])
            if node.right:
                q.append([node.right, node.val, parent])
        return val

