# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        def iterate(root, subroot):
            if not root:
                return False
            
            if root.val == subroot.val:
                if checkSame(root, subroot):
                    return True
            
            return iterate(root.left, subroot) or iterate(root.right, subroot)
        

        def checkSame(root, subroot):
            if (root and not subroot) or (subroot and not root):
                return False
            if not root:
                return True
            
            if root.val != subroot.val:
                return False
            
            return checkSame(root.left, subroot.left) and checkSame(root.right, subroot.right)
            

        return iterate(root, subroot)
        