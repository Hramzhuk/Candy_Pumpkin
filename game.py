import pygame
from time import sleep
pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Candy Pumpkin")

GREEN = (0, 128 ,0)
GREY = (128, 128, 128)
BLUE = (66, 170, 255)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)

FPS = 60
clock = pygame.time.Clock()

x = 0
y = 330
speed = 5

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    # if keys[pygame.K_UP]:
    #     y -= speed
    #     pygame.display.update()
    #     pygame.time.delay(600)
    #     y += speed
    #     pygame.display.update()


    sc.fill(BLACK)
    pygame.draw.rect(sc, GREEN, (0, 350, 600, 50))
    pygame.draw.circle(sc, GREY, (550, 50), 30)
    pygame.draw.rect(sc, ORANGE, (x, y, 10, 20))
    pygame.display.update()

    clock.tick(FPS)