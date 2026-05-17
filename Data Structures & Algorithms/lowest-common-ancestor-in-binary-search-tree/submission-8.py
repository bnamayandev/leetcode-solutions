# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, node: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val >= q.val:
            hi = p
            low = q
        
        else:
            hi = q
            low = p
            
        while True:
            if node and node.val >= low.val and node.val <= hi.val:
                return node
            
            else:
                if node.val > hi.val:
                    node = node.left
                else:
                    node = node.right