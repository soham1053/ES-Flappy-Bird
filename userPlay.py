from constants import *
from game import FlappyBird
import pygame

pygame.init()

screen = pygame.display.set_mode((screenWidth, screenHeight))

fps = 30
clock = pygame.time.Clock()

numBirds = 4
game = FlappyBird(3, numBirds, separateBirds=True)

jumps = [False for _ in range(numBirds)]
pressing = [False for _ in range(numBirds)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game.reset()

    keys = pygame.key.get_pressed()
    for i in range(numBirds):
        exec("jumps[i] = keys[pygame.K_" + chr(i+97) + "] and not pressing[i]")
        exec("pressing[i] = keys[pygame.K_" + chr(i+97) + "]")

    game.step(jumps)

    game.draw(screen, mode="human")
    pygame.display.flip()

    clock.tick(fps)