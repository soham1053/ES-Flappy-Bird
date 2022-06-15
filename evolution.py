from constants import *
from game import FlappyBird
from population import Population
import pygame

pygame.init()

screen = pygame.display.set_mode((screenWidth, screenHeight))

iterations = 1000
gamesPerIteration = 1

numBirds = 100
game = FlappyBird(3, numBirds, separateBirds=False)

pop = Population(numBirds, game.inputSize)

for iter in range(iterations):
    for i in range(gamesPerIteration):
        states = game.reset()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            jumps = pop.act(states)

            states, done = game.step(jumps)

            game.draw(screen, mode="computer")
            pygame.display.flip()
        pop.store(game.getPoints())
    pop.evolve()
