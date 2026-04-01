# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def dfs(self, curr, s):
        if not curr:
            s.append('*')
            return
        s.append(str(curr.val))
        self.dfs(curr.left, s)
        self.dfs(curr.right, s)

    def serialize(self, root):
        s = []
        self.dfs(root, s)
        return ','.join(s)

    def decode(self, data_list):
        if not data_list:
            return None
        val = data_list.pop(0)
        if val == '*':
            return None
        node = TreeNode(int(val))
        node.left = self.decode(data_list)
        node.right = self.decode(data_list)
        return node

    def deserialize(self, data):
        if not data:
            return None
        data_list = data.split(',')
        return self.decode(data_list)
# Example usage:
# codec = Codec()
# serialized = codec.serialize(root)
# new_root = codec.deserialize(serialized)