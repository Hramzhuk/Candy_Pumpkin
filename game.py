import pygame
from time import sleep
pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Candy Pumpkin")

GREEN = (0, 128, 0)
WHITE_ORANGE = (255, 238, 202)
BLUE = (0, 49, 83)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
PINK = (255, 192, 203)
WHITE = (255, 255, 255)
GREY = (165, 165, 165)

FPS = 60
clock = pygame.time.Clock()

x = 0
y = 330
speed = 5
health = 10

f = pygame.font.SysFont("arial", 24)
sc_text = f.render("Health: " + str(health), 1, WHITE)
pos = sc_text.get_rect(center=(50, 20))
player = pygame.draw.rect(sc, ORANGE, (x, y, 10, 20))
thorns = pygame.draw.rect(sc, GREY, (200, 350, 100, 5))
game_over = False
obstacles = {"thorns": 1}

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and game_over == False:
        x -= speed
    if keys[pygame.K_RIGHT] and game_over == False:
        x += speed
    # if keys[pygame.K_UP]:
    #     y -= speed
    #     pygame.display.update()
    #     pygame.time.delay(600)
    #     y += speed
    #     pygame.display.update()
    if player.x == 200:
        health -= obstacles["thorns"]

    if game_over == False:
        sc.fill(BLUE)
        pygame.draw.rect(sc, GREEN, (0, 350, 600, 50))
        pygame.draw.circle(sc, WHITE_ORANGE, (550, 50), 30)
        player = pygame.draw.rect(sc, ORANGE, (x, y, 10, 20))
        thorns = pygame.draw.rect(sc, GREY, (200, 350, 100, 5))
        f = pygame.font.SysFont("arial", 24)
        sc_text = f.render("Health: " + str(health), 1, WHITE)
        pos = sc_text.get_rect(center=(50, 20))
        game_over_text = f.render("Game Over!", 1, WHITE)
        game_over_text_pos = game_over_text.get_rect(center=(W//2, H//2))
        sc.blit(sc_text, pos)
        if health == 0:
            sc.fill(BLACK)
            sc.blit(game_over_text, game_over_text_pos)
            game_over = True
        pygame.display.update()

    clock.tick(FPS)