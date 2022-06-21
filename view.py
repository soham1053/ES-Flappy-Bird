from constants import *
from game import FlappyBird
from population import Agent
import pygame

pygame.init()

screen = pygame.display.set_mode((screenWidth, screenHeight))

fps = 30
clock = pygame.time.Clock()

game = FlappyBird(3, 1, separateBirds=False)

agent = Agent(game.inputSize)
agent.load("policy")

state = game.reset()[0]
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    state, done = game.step(agent.act(state))
    state = state[0]

    game.draw(screen, mode="computer")
    pygame.display.flip()

    clock.tick(fps)

print(game.birds[0].points)