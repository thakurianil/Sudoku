import random

class Generate_Game:
    def __init__(self):
        self.sudoku = []
        self.matrix = []
        self.matrix1 = []
        self.matrix2 = []
        self.matrix3 = []


    def generate_sudoku(self):
        num = []
        b = random.randint(1, 2)
        if b == 1:
            for x in range(0, 1):
                self.matrix.append([])
                unique_random = random.sample("123456789", 9)
                for y in unique_random:
                    num.append(int(y))
                for z in range(0, 9):
                    self.matrix[x].append(num[z])

            for x in range(1, 3):
                self.matrix.append([])
                for y in range(0, 9):
                    self.matrix[x].append(self.matrix[x - 1][(y - 3) % 9])

            for x in range(3, 4):
                self.matrix.append([])
                for y in range(0, 9):
                    self.matrix[x].append(self.matrix[x - 1][(y - 1) % 9])

            for x in range(4, 6):
                self.matrix.append([])
                for y in range(0, 9):
                    self.matrix[x].append(self.matrix[x - 1][(y - 3) % 9])

            for x in range(6, 7):
                self.matrix.append([])
                for y in range(0, 9):
                    self.matrix[x].append(self.matrix[x - 1][(y - 1) % 9])

            for x in range(7, 9):
                self.matrix.append([])
                for y in range(0, 9):
                    self.matrix[x].append(self.matrix[x - 1][(y - 3) % 9])
        else:
            for x in range(0, 1):
                self.matrix.append([])
                unique_random = random.sample("123456789", 9)
                for y in unique_random:
                    num.append(int(y))
                for z in range(0, 9):
                    self.matrix[x].append(num[z])

            for x in range(1, 3):
                self.matrix.append([])
                for y in range(0, 9):
                    self.matrix[x].append(self.matrix[x - 1][(y + 3) % 9])

            for x in range(3, 4):
                self.matrix.append([])
                for y in range(0, 9):
                    self.matrix[x].append(self.matrix[x - 1][(y + 1) % 9])

            for x in range(4, 6):
                self.matrix.append([])
                for y in range(0, 9):
                    self.matrix[x].append(self.matrix[x - 1][(y + 3) % 9])

            for x in range(6, 7):
                self.matrix.append([])
                for y in range(0, 9):
                    self.matrix[x].append(self.matrix[x - 1][(y + 1) % 9])

            for x in range(7, 9):
                self.matrix.append([])
                for y in range(0, 9):
                    self.matrix[x].append(self.matrix[x - 1][(y + 3) % 9])


        return self.matrix


    def remove_digit(self, difficulty):
        num = []
        self.sudoku = self.generate_sudoku()

        for x in range(0, 9):
            self.matrix3.append([])
            for y in range(0, 9):
                self.matrix3[x].append([])
        for x in range(0, 9):
            for y in range(0, 9):
                self.matrix3[x][y] = self.sudoku[x][y]

        for x in range(0, 9):
            unique_random = random.sample("012345678", difficulty)
            for y in unique_random:
                num.append(int(y))
            for z in range(0, len(num)):
                self.sudoku[x][num[0]] = 0
                num.pop(0)

        for x in range(0, 9):
            self.matrix1.append([])
            for y in range(0, 9):
                self.matrix1[x].append(False)
        for x in range(0, 9):
            for y in range(0, 9):
                if self.sudoku[x][y] == 0:
                    self.matrix1[x][y] = True

        for x in range(0, 9):
            self.matrix2.append([])
            for y in range(0, 9):
                self.matrix2[x].append([])
        for x in range(0, 9):
            for y in range(0, 9):
                self.matrix2[x][y] = self.sudoku[x][y]


        return self.sudoku
