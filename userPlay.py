from constants import *
from game import FlappyBird
import pygame

pygame.init()

screen = pygame.display.set_mode((screenWidth, screenHeight))

fps = 30
clock = pygame.time.Clock()

numBirds = 4
game = FlappyBird(3, numBirds, separateBirds=True)

jumpsString = "jumps = ["
for i in range(numBirds):
    jumpsString += "event.key == pygame.K_" + chr(i+97) + ", "
jumpsString = jumpsString[:-2] + "]"
print(jumpsString)

while True:
    jumps = [False for _ in range(numBirds)]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            exec(jumpsString)
            if event.key == pygame.K_RETURN:
                game.reset()

    game.step(jumps)

    game.draw(screen, mode="human")
    pygame.display.flip()

    clock.tick(fps)