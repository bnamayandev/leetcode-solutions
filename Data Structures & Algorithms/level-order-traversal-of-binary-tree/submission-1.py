# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []

        queue = deque([root])

        while queue:
            level_size = len(queue)

            current_level = []

            for _ in range(level_size):
                n = queue.popleft()
                current_level.append(n.val)

                if n.left:
                    queue.append(n.left)
                
                if n.right:
                    queue.append(n.right)
            
            result.append(current_level)

        return result