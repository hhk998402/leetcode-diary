class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [{} for x in range(9)]
        columns = [{} for x in range(9)]
        rows = [{} for x in range(9)]
        for i in range(9):
            for j in range(9):
                box_idx = (i//3)*3 + j//3
                ele = board[i][j]
                if(not ele.isdigit()):
                    continue
                if(ele in boxes[box_idx] or ele in columns[j] or ele in rows[i]):
                    print(ele, i,j, boxes[box_idx], columns[j], rows[i])
                    return False
                boxes[box_idx][ele] = 1
                columns[j][ele] = 1
                rows[i][ele] = 1
        return True
