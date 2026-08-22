# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.

    def dfs(self, current, s):
        if not current:
            s.append("*")
            return

        s.append(str(current.val))

        self.dfs(current.left, s)
        self.dfs(current.right, s)



    def decode(self, data_list):
        if not data_list:
            return None

        value = data_list.pop(0)

        if value == "*":
            return None

        node = TreeNode(int(value))
        node.left = self.decode(data_list)
        node.right = self.decode(data_list)

        return node

    def serialize(self, root: Optional[TreeNode]) -> str:
        s = []
        self.dfs(root, s)
        return ",".join(s)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        data_list = data.split(",")
        return self.decode(data_list)