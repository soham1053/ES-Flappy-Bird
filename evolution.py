from constants import *
from game import FlappyBird
from population import Population
import pygame

pygame.init()

# When render is true, the flappy bird screen is shown while training
# When loadPrevPolicy is true, the training starts with whatever policy.pt contains
render = True
loadPrevPolicy = False

if render:
    screen = pygame.display.set_mode((screenWidth, screenHeight))

iterations = 10000
gamesPerIteration = 1

numBirds = 100
game = FlappyBird(3, numBirds, separateBirds=False)

pop = Population(numBirds, game.inputSize)
if loadPrevPolicy:
    pop.load("policy")

for iter in range(iterations):
    for i in range(gamesPerIteration):
        states = game.reset()
        done = False
        while not done:
            if render:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

            jumps = pop.act(states, game.getDead())

            states, done = game.step(jumps)

            if render:
                game.draw(screen, mode="computer")
                pygame.display.flip()
        pop.store(game.getPoints())
    pop.evolve()
