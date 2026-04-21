# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):
        in_order_list = []

        self.helper(root, in_order_list)

        # check if sorted strictly increasing
        for i in range(1, len(in_order_list)):
            if in_order_list[i] <= in_order_list[i - 1]:
                return False

        return True

    def helper(self, node, in_order_list):
        if node is None:
            return

        self.helper(node.left, in_order_list)
        in_order_list.append(node.val)
        self.helper(node.right, in_order_list)