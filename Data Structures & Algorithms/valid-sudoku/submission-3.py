class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Validate rows 
        for i in range(9):
            dups = set()
            for j in range(9):
                if board[i][j] in dups:
                    return False
                elif board[i][j] == ".":
                    continue
                else:
                    dups.add(board[i][j])

        #Validate columns 
        for i in range(9):
            dups = set()
            for j in range(9):
                if board[j][i] in dups:
                    return False
                elif board[j][i] == ".":
                    continue
                else:
                    dups.add(board[j][i])
        
        #Validate boxes
        start = [(0,0), (0,3), (0,6),
                (3,0), (3,3), (3,6),
                (6,0), (6,3), (6,6)]
        for i, j in start:
            dups = set()
            for k in range(i, i+3):
                for z in range(j, j+3):
                    if board[k][z] in dups:
                        return False
                    elif board[k][z] == ".":
                        continue
                    else:
                        dups.add(board[k][z])
        return True 




        