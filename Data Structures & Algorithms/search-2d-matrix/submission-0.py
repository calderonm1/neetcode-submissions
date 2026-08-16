import math

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m * n

        print("m:", m, "n:", n)
        print()

        while l < r:
            cell = (l + r) // 2
            row = cell // n
            col = cell % n

            val = matrix[row][col]

            print(f"cell_{cell}:", matrix[row][col])
            print("row:", row, "col:", col)
            print()

            if val == target:
                return True
            elif val > target:
                r = cell
            else:
                l = cell + 1

        return False