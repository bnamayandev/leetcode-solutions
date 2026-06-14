# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        levels = [[root.val]]
        q = deque([root])

        while q:
            curr_level_values = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    curr_level_values.append(node.left.val)
                    q.append(node.left)
                if node.right:
                    curr_level_values.append(node.right.val)
                    q.append(node.right)
            if curr_level_values:
                levels.append(curr_level_values)
        
        return [r[-1] for r in levels]