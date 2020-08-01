class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        return (self.are_rows_valid(board) and self.are_cols_valid(board) and self.are_sub_boxes_valid(board))
        
    def is_valid_portion(self, portion):
        portion = [i for i in portion if i != '.']
        return len(portion) == len(set(portion))

    def are_rows_valid(self, board):
        for row in board:
            if not self.is_valid_portion(row):
                return False
        return True

    def are_cols_valid(self, board):
        for i in range(0,9):
            col = [row[i] for row in board]
            if not self.is_valid_portion(col):
                return False
        return True

    def are_sub_boxes_valid(self, board):
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                square = [board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
                if not self.is_valid_portion(square):
                    return False
        return True       
