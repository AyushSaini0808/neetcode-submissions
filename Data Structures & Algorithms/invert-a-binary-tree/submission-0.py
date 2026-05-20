# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(root):
            if not root:
                return None
            q=deque()
            q.append(root)
            while q:
                temp=q.popleft()
                temp.right,temp.left=temp.left,temp.right
                if temp.right:q.append(temp.right)
                if temp.left:q.append(temp.left)
            return root
        return bfs(root)