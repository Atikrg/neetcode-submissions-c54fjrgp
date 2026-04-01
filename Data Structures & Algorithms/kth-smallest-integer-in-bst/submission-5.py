# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root: TreeNode, k: int, counter: list) -> TreeNode:
        if root is None:
            return None

        node = self.helper(root.left, k, counter)  # Traverse the left subtree
        if node:
            return node

        counter[0] += 1  # Increment the counter when visiting a node
        if counter[0] == k:
            return root

        return self.helper(root.right, k, counter)  # Traverse the right subtree

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        counter = [0]  # List to hold the counter reference
        node = self.helper(root, k, counter)
        return node.val if node else -1