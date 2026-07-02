class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num=board[i][j]
                if num==".":
                    continue

                if num in row[i]:
                    return False
                else:
                    row[i].add(num)

                if num in col[j]:
                    return False
                else:
                    col[j].add(num)

                sub=(i//3)*3+(j//3)
                if num in box[sub]:
                    return False
                else:
                    box[sub].add(num)
        return True
                

        