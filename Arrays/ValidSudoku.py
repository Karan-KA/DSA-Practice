# Problem: Valid Sudoku
# Time Complexity: O(n^2)
# Space Complexity: 




# Board dimenstion 9 x 9
# Valid if each rows, coloumns and sub boxes of dimenstion(3x3) has no duplicate elements

class Solution:
    def validSudoku(self, board):

        # use three hashsets for rows, columns and sub boxes to check for the duplicate

        rows = [set() for i in range(9)]
        columns = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):

                val = board[i][j]

                box_idx = (i//3) * 3 + (j//3)

                if val == '.':
                    continue

                if val in rows[i] or val in columns[j] or val in boxes[box_idx]:
                    return False
                
                rows[i].add(val)
                columns[j].add(val)
                boxes[box_idx].add(val)

        return True