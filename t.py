import pygame
import random
import copy


pygame.init()  # активируем модули pygame

# создание элементов сетки
I_max = 11
J_max = 21

# размер экрана
screen_x = 300
screen_y = 600

# создание экрана
screen = pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()
pygame.display.set_caption('Tetris Best')

# ширина и высота каждой ячейки
dx = screen_x/(I_max - 1)
dy = screen_y/(J_max - 1)

fps = 60
grid = []  # список который хранит параметры сетки

for i in range(0, I_max):
    grid.append([])
    for j in range(0, J_max):
        grid[i].append([1])

for i in range(0, I_max):
    for j in range(0, J_max):
        grid[i][j].append(pygame.Rect(i * dx, j * dy, dx, dy))
        grid[i][j].append(pygame.Color('Black'))


details = [
    [[-2, 0], [-1, 0], [0, 0], [1, 0]],
    [[-1, 1], [-1, 0], [0, 0], [1, 0]],
    [[1, 1], [-1, 0], [0, 0], [1, 0]],
    [[-1, 1], [0, 1], [0, 0], [-1, 0]],
    [[1, 0], [1, 1], [0, 0], [-1, 0]],
    [[0, 1], [-1, 0], [0, 0], [1, 0]],
    [[-1, 1], [0, 1], [0, 0], [1, 0]],
]

# создание деталей 7 шт.
det = [[], [], [], [], [], [], [],]
for i in range(0, len(details)):
    for j in range(0, 4):
        det[i].append(pygame.Rect(details[i][j][0] * dx + dx * (I_max // 2), details[i][j][1] * dy, dx, dy))

detail = pygame.Rect(0, 0, dx, dy)
det_choice = copy.deepcopy(random.choice(det))
count = 0

game = True
while game:
    delta_x = 0
    delta_y = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                delta_x = -1
            elif event.key == pygame.K_RIGHT:
                delta_x = 1

    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN]:
        count = 31 * fps

    screen.fill(pygame.Color('Gray'))

    for i in range(0, I_max):
        for j in range(0, J_max):
            pygame.draw.rect(screen, grid[i][j][2], grid[i][j][1], grid[i][j][0])

    # обозначение границ поля и деталей
    for i in range(4):
        if (det_choice[i].x + delta_x * dx < 0) or (det_choice[i].x + delta_x * dx >= screen_x):
            delta_x = 0
        if (det_choice[i].y + dy >= screen_y) or (grid[int(det_choice[i].x // dx)][int(det_choice[i].y // dy) + 1]
                                                  [0] == 0):
            delta_y = 0
            for i in range(4):
                x = int(det_choice[i].x // dx)
                y = int(det_choice[i].y // dy)
                grid[x][y][0] = 0  # закрашиваем квадратик
                grid[x][y][2] = pygame.Color('Orange')
            detail.x = 0
            detail.y = 0
            det_choice = copy.deepcopy(random.choice(det))  # копируем детали

    # передвижение по х
    for i in range(4):
        det_choice[i].x += delta_x * dx

    count += fps  # исключаем слишком быстрое передвижение по у
    # передвижение по y
    if count > 30 * fps:
        for i in range(4):
            det_choice[i].y += delta_y * dy
        count = 0

    for i in range(4):
        detail.x = det_choice[i].x
        detail.y = det_choice[i].y
        pygame.draw.rect(screen, pygame.Color('White'), detail)

    pygame.display.flip()
    clock.tick(fps)
