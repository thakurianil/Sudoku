import pygame
from Generate import *
from Play import *
from Hint import *
from Solve import *

def display_line():
    for x in range(0, 10):
        if x == 0 or x == 3 or x == 6 or x == 9:
            pygame.draw.line(window, black, (x * size + windowadd / 5, windowadd),
                             (x * size + windowadd / 5, Windowsize + windowadd), 3)
            pygame.draw.line(window, black, (windowadd / 5, x * size + windowadd),
                             (Windowsize + windowadd / 5, x * size + windowadd), 3)
        else:
            pygame.draw.line(window, black, (x * size + windowadd / 5, 0 + windowadd),
                             (x * size + windowadd / 5, Windowsize + windowadd))
            pygame.draw.line(window, black, (0 + windowadd / 5, x * size + windowadd),
                             (Windowsize + windowadd / 5, x * size + windowadd))



pygame.init()

g = Generate_Game()
p = Play_Game()
h = Hint_Game()

Test = True

Windowsize = 450
windowadd = 150
window = pygame.display.set_mode((Windowsize + windowadd / 2, Windowsize + (3*windowadd)/2))
size = Windowsize/9

black = (0, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
green = (50, 205, 50)
yellow = (255, 255, 0)
red = (255, 0, 0)


myFont = pygame.font.SysFont("Times New Roman", size-2)
myFont2 = pygame.font.SysFont("Chiller", size-2)
myFont3 = pygame.font.SysFont("Agency FB", size-2)

pygame.display.set_caption("Sudoku : Mind Game")
image1 = pygame.image.load("images/logo.jpg").convert_alpha()
image2 = pygame.image.load("images/l.jpg").convert_alpha()
image3 = pygame.image.load("images/3.png").convert_alpha()
pygame.mixer.music.load("sounds/PySudokuTheme1.ogg")


def display_digit(sudoku):
    for x in range(0, 9):
        for y in range(0, 9):
            if sudoku[x][y] != 0:
                if g.matrix1[x][y]:
                    text = myFont.render(str(sudoku[x][y]), 1, black)
                else:
                    text = myFont.render(str(sudoku[x][y]), 1, blue)
                window.blit(text, ((y * size + windowadd / 5) + size / 5, x * size + windowadd))

window.fill(white)
text1 = myFont2.render(str("Easy"), 1, black)
Easy_button = pygame.draw.rect(window, (green), ((Windowsize) / 2 - 25, windowadd, windowadd, windowadd / 2));
window.blit(text1,((Windowsize) / 2 + 20, windowadd + 10))
text2 = myFont2.render(str("Medium"), 1, black)
Medium_button = pygame.draw.rect(window, (yellow), (Windowsize / 2 - 25, 2 * windowadd, windowadd, windowadd / 2));
window.blit(text2,((Windowsize) / 2, 2 * windowadd + 10))
text3 = myFont2.render(str("Hard"), 1, black)
Hard_button = pygame.draw.rect(window, (red), (Windowsize / 2 - 25, 3 * windowadd, windowadd, windowadd / 2));
window.blit(text3,((Windowsize) / 2 + 20, 3 * windowadd + 10))
window.blit(image1, ((2 * windowadd) / 3, 10))
text4 = myFont2.render(str("Solve"), 1, black)
text5 = myFont2.render(str("Solved"), 1, black)
text6 = myFont2.render(str("Hint"), 1, black)

pygame.mixer.music.play(2, 0.0)

play = False
menu = True
hint = True
test2 = False
test3 = False
d = 0
while menu:

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pressed1 = pygame.mouse.get_pressed()

        if pressed1 and Test:

            if Easy_button.collidepoint(pos):
                window.fill(white)
                g.remove_digit(5)
                display_line()
                display_digit(g.sudoku)

                play = True
                Test = False

            elif Medium_button.collidepoint(pos):
                window.fill(white)
                g.remove_digit(6)
                display_line()
                display_digit(g.sudoku)

                play = True
                Test = False

            elif Hard_button.collidepoint(pos):
                window.fill(white)
                g.remove_digit(7)
                display_line()
                display_digit(g.sudoku)

                play = True
                Test = False

    if play:
        solve = pygame.draw.rect(window, (red), (385, 615, 100, 50));
        Hint = pygame.draw.rect(window, (red), (25, 615, 100, 50));
        window.blit(text6, (45, 615))
        window.blit(text4, (395, 615))

        window.blit(image1, ((2 * windowadd) / 3, 10))
        (check, x, y) = pygame.mouse.get_pressed()
        if check and test2:
            (x, y) = pygame.mouse.get_pos()
            if x > 30 and y > 150 and x < 480 and y < 600:
                a = x - windowadd / 5
                b = y - windowadd
                x = a / size
                y = b / size
                test2 = p.play_sudoku(g.sudoku, g.matrix1, y, x)
                window.fill(white)
                display_line()
                display_digit(g.sudoku)


        if check and test3:
            if Hint.collidepoint(pos) and pressed1:
                s = 0
                t = 0
                test3 = h.hint_sudoku(g.sudoku, g.matrix3, s, t)

                window.fill(white)
                display_line()
                display_digit(g.sudoku)

        if check == False:
            test2 = True
            test3 = True

        if solve.collidepoint(pos) and pressed1:
            window.fill(white)
            display_line()
            for x in range(0, 9):
                for y in range(0, 9):
                    if g.sudoku[x][y] != g.matrix3[x][y]:
                        g.sudoku[x][y] = 0

            play = False
            solve_sudoku(g.sudoku)
            display_digit(g.sudoku)
            window.blit(image2, ((2 * windowadd) / 3, 10))
            solve = pygame.draw.rect(window, (red), (400, 620, 100, 50));
            window.blit(text5, (410, 620))
            pygame.mixer.music.play(9, 0.0)







