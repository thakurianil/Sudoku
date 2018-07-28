class Play_Game:

    # def __init__(self):


    def play_sudoku(self,sudoku,matrix1,y,x):

        if matrix1[y][x]:
            sudoku[y][x] = sudoku[y][x] % 9 + 1
            return False