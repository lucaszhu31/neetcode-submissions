class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Validate row:
        for row in board:
            duplicates = set()
            for num in row:
                if num != ".":
                    if num in duplicates:
                        return False 
                    else:
                        duplicates.add(num)

        #Validate columns:
        for i in range(9):
            duplicates = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in duplicates:
                        return False
                    else:
                        duplicates.add(board[j][i])

        #Validate boxes
        indexes = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]
        for i, j in indexes:
            duplicates = set()
            for x in range(i, i+3):
                for y in range(j, j+3):
                    if board[x][y] != ".":
                        if board[x][y] in duplicates:
                            return False
                        else:
                            duplicates.add(board[x][y])

        return True 



                    
            

