class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def fun(i,j,index):
            if index==len(word):
                return True
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]!=word[index]:
                return False
            a=board[i][j]
            board[i][j]="*"
            z=fun(i+1,j,index+1) or fun(i-1,j,index+1) or fun(i,j-1,index+1) or fun(i,j+1,index+1)
            board[i][j]=a
            return z
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if fun(i,j,0):
                        return True
        return False