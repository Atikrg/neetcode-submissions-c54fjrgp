class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False


    def addWord(self, word):
        current = self
        for c in word:

            if c not in current.children:
                current.children[c] = TrieNode()

            current = current.children[c] 

        current.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()

        for c in words:
            root.addWord(c);



        rows = len(board)
        cols = len(board[0])


        result = set()
        visit = set()



        def dfs(r, c, node, word):

            if(r< 0 or c < 0 or r == rows or
                c == cols or (r, c) in visit or board[r][c] not  in node.children):
                return

            visit.add((r, c))


            node = node.children[board[r][c]]

            word += board[r][c]

            if node.isWord:
                result.add(word)

            dfs(r -1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            visit.remove((r, c))





        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root, "")


        return list(result)



        