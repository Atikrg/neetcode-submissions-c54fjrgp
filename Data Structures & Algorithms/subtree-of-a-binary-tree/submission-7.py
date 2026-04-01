# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def preOrderTraversal(self, node):
        if node is None:
            return "None"

        result = str(node.val)
        result += self.preOrderTraversal(node.left)
        result += self.preOrderTraversal(node.right)

        return result

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        full_tree = self.preOrderTraversal(root)
        sub_tree = self.preOrderTraversal(subRoot)

        return sub_tree in full_tree
        