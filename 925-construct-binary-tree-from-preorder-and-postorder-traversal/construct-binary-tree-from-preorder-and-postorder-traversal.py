# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        mapp = {}
        for i, num in enumerate(postorder):
            mapp[num] = i
        def help(i1,i2,j1,j2):
            if j1 > j2 or i1> i2:
                return None
            root = TreeNode(preorder[i1])
            if i1 != i2:
                leftval = preorder[i1 + 1]
                mid = mapp[leftval]
                size = mid - j1 + 1
                root.left = help(i1+1,i1 + size,j1, mid)
                root.right = help(i1+ 1+ size,i2,mid + 1, j2 -1)
            return root

        return help(0,n-1,0,n-1)