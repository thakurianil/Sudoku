import random
class Hint_Game:

    def __init__(self):
        self.hintsx = []
        self.hintsy = []
        self.count = 5


    def hint_sudoku(self, sudoku, matrix3,s ,t):
        self.hintsx = []
        self.hintsy = []

        for x in range(0, 9):
            for y in range(0,9):
                if sudoku[x][y] == 0:
                    self.hintsx.append(x)
                    self.hintsy.append(y)


        if len(self.hintsx) == 0:
            window.blit(image2, ((2 * windowadd) / 3, 10))
            solve = pygame.draw.rect(window, (red), (400, 620, 100, 50));
            window.blit(text5, (410, 620))
            pygame.mixer.music.play(9, 0.0)

            return False
        if self.count > 0:
            self.select_hints(sudoku,matrix3)
            self.count -= 1


    def select_hints(self,sudoku, matrix3):
        c = random.randrange(len(self.hintsx))
        x = matrix3[self.hintsx[c]][self.hintsy[c]]
        sudoku[self.hintsx[c]][self.hintsy[c]] = x
        del(self.hintsx[c])
        del(self.hintsy[c])

        return False
