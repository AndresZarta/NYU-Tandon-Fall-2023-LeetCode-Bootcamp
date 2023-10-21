class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        last_row_index = len(grid) - 1
        last_row = grid[last_row_index]
        length = len(last_row) 

        for column in range(length - 2, -1, -1):
            last_row[column] = last_row[column + 1] + last_row[column]

        for row in range(last_row_index - 1, -1, -1):
            current_row = grid[row]
            right = float("inf")
            for i in range(length - 1, -1, -1):
                current_row[i] = min(right, last_row[i]) + current_row[i]
                right = current_row[i]
            last_row = current_row
        return last_row[0]
