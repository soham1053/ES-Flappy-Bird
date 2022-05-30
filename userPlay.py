from constants import *
from game import FlappyBird
import pygame

pygame.init()

screen = pygame.display.set_mode((screenWidth, screenHeight))

fps = 30
clock = pygame.time.Clock()

game = FlappyBird(3)

while True:
    jump = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump = True
            elif event.key == pygame.K_RETURN:
                game.reset()


    game.step(jump)

    game.draw(screen)
    pygame.display.flip()

    clock.tick(fps)