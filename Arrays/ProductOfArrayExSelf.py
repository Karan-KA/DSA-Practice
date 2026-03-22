# Problem: Product of Array Exccept self
# Time complexity: O(n)
# Space Complexit: O(n)

class Solution:
    def productExceptSelf(self, nums):

        ans = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans


class Solution:
    def isValidSudoku(self, board) -> bool:

        rows = [set() for i in range(9)]
        columns = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for i in range(len(board)):
            for j in range(len(board)):

                val = board[i][j]

                if val == '.':
                    continue

                idx = (i//3)*3 + (j//3)
                
                if val in rows[i] or val in columns[j] or val in boxes[idx]:
                    return False

                rows[i].add(val)
                columns[j].add(val)
                boxes[idx].add(val)
        return True

s = Solution()
result =s.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])

print(result)