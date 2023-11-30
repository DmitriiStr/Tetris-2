import pygame
import random
import copy


pygame.init()

# создание сетки
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
