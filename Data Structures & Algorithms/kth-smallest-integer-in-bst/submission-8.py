# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = [0]


        node = self.helper(root, counter, k)

        return node.val if not None else -1


    
    def helper(self, root, counter, k):
        if not root:
            return None

        node = self.helper(root.left, counter, k)

        if node:
            return node

        counter[0] += 1

        if counter[0] == k:
            return root


        return self.helper(root.right, counter, k)
