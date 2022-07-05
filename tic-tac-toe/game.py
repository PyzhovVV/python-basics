import pygame
from random import randint
from numpy import diagonal, fliplr


def check_losing(mas, sign):  # определение ситуации на поле (проигрыш, ничья, игра продолжается)
    count_zeros = 0
    for row in mas:  # проверка проигрыша по горизонтали
        count_zeros += row.count(0)
        if sign * 5 in ''.join((map(str, row))):
            return sign
    for row in range(len(mas)):  # проверка проигрыша по вертикали
        single_column = [mas[column][row] for column in range(len(mas))]
        if sign * 5 in ''.join((map(str, single_column))):
            return sign
    for i in range(-10, 10):  # проверка проигрыша по диагоналям
        if sign * 5 in ''.join((map(str, diagonal(mas, i)))) \
                or sign * 5 in ''.join(map(str, diagonal(fliplr(mas), i))):
            return sign
    if count_zeros == 0:  # если свободных клеток на поле не осталось
        return 'Ничья'
    return False


def find_coordinates():  # нахождение координат нажатой клетки
    x_mouse, y_mouse = pygame.mouse.get_pos()  # считывание координат курсора
    column = x_mouse // (size_block + margin)  # перевод координат в номер столбца
    row = y_mouse // (size_block + margin)  # перевод координат в номер строки
    return row, column


def computer_moving(mas, game_over):
    trying = True
    while trying:
        rand_x, rand_y = randint(0, len(mas) - 1), randint(0, len(mas) - 1)
        if mas[rand_x][rand_y] == 0 and not check_losing(mas, 'o'):  # компьютер ставит нули рандомно,
            # но проверяет, чтобы не поставить его 5-м в ряд, строку или диагональ
            mas[rand_x][rand_y] = 'o'
            trying = False
            game_over = check_losing(mas, 'o')
    return mas, game_over

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
size_block = 40
margin = 5
running = True
mas = [[0] * 10 for _ in range(10)]
width = height = size_block * 10 + margin * 11
query = 0
game_over = False
pygame.init()
screen = pygame.display.set_mode((455, 455))
pygame.display.set_caption("Обратные крестики нолики")
clock = pygame.time.Clock()
screen.fill(black)
pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:  # ситуация нажатия на клетку
            row, column = find_coordinates()
            if mas[row][column] == 0:  # определение кто ходит (ставить крестик или ноилк)
                mas[row][column] = 'x'
                game_over = check_losing(mas, 'x')
                if not game_over:
                    mas, game_over = computer_moving(mas, game_over)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # перезапуск игры нажатием пробела
            game_over = False
            mas = [[0] * 10 for _ in range(10)]
            query = 0
            screen.fill(black)
    for row in range(10):
        for column in range(10):
            x = size_block * column + (column + 1) * margin  # определение координат для клеток
            y = size_block * row + (row + 1) * margin  # определение координат для клеток
            pygame.draw.rect(screen, white, (x, y, size_block, size_block))  # прорисовка клеток
            if mas[row][column] == 'x':  # рисование крестика в клетке
                pygame.draw.line(screen, black, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 4)
                pygame.draw.line(screen, black, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5), 4)
            elif mas[row][column] == 'o':  # рисование нолика в клетке
                pygame.draw.circle(screen, black, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3, 3)
    if game_over:  # прорабатывание ситуации окончания игры
        screen.fill(black)
        font = pygame.font.SysFont('stxingkai', 90)
        text1 = font.render(game_over, True, white)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2  # нахождения геометрического центра
        text_y = screen.get_height() / 2 - text_rect.height / 2  # нахождения геометрического центра
        screen.blit(text1, [text_x, text_y])
    pygame.display.update()
