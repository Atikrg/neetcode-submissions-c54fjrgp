# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def helper(self, root, k, counter):
        if not root:
            return None

        node = self.helper(root.left, k, counter)

        if node:
            return node

        counter[0] +=1
        
        if counter[0] == k:
            return root

        return self.helper(root.right, k, counter)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = [0]
        node = self.helper(root, k, counter)

        return node.val if node else -1