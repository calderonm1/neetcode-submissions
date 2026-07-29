class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_nums = [0] * 9
        col_nums = [0] * 9
        box_nums = [0] * 9

        for x in range (len(board)):
            for y in range(len(board[x])):
                box_idx = (3 * (x // 3)) + (y // 3)

                if (board[x][y] == "."):
                    continue
                
                col_nums[y] += 10 ** (int(board[x][y]) - 1)
                row_nums[x] += 10 ** (int(board[x][y]) - 1)
                box_nums[box_idx] += 10 ** (int(board[x][y]) - 1)

        for num in row_nums + col_nums + box_nums:
            try: int(str(num), 2)
            except ValueError:
                return False
        return True

        
        

