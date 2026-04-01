class Solution:

    def dfs(self,board, word, pos, col,row):

        if(pos == len(word)):
            return True

        if(row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != word[pos]):
            return False

        letter = board[row][col]
        board[row][col] = "#"
        found = (self.dfs(board, word, pos+1, col+1, row) or 
                self.dfs(board, word, pos + 1, col - 1,row) or 
                self.dfs(board, word, pos + 1, col, row + 1) or 
                self.dfs(board, word, pos + 1, col, row - 1))
        board[row][col] = letter

        return found
        
        

    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0] and self.dfs(board, word, 0, col, row):
                    return True
        return False