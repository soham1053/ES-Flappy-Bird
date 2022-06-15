from bird import Bird
from pipe import Pipe
from constants import *
import numpy as np
import torch
import pygame

class FlappyBird:
    def __init__(self, numPipes, numBirds, separateBirds):
        self.pipes = self.makePipes(numPipes)

        self.separateBirds = separateBirds
        if separateBirds:
            self.birds = [Bird(i * Bird.img.get_size()[0] * 1.2) for i in range(numBirds)]
        else:
            self.birds = [Bird(birdX) for _ in range(numBirds)]

        self.inputSize = 2 + 2 * numPipes

        self.started = False
        self.font = pygame.font.SysFont("Impact", 40, False)

    def reset(self):
        self.__init__(len(self.pipes), len(self.birds), self.separateBirds)
        return self.states()

    def step(self, jumps):
        if not self.started:
            self.started = True
            for bird in self.birds:
                bird.move(True)

        else:
            for bird, jump in zip(self.birds, jumps):
                if self.collision(bird) or bird.hitGround():
                    bird.die()

                if self.birdInPipe(bird):
                    bird.enterPipe()
                elif not self.birdInPipe(bird):
                    bird.leavePipe()

                bird.move(jump)

        for pipe in self.pipes:
            pipe.move()

        return self.states(), not any([not bird.dead for bird in self.birds])

    def states(self):
        pipeState = []
        for pipe in self.pipes:
            pipeState.extend([pipe.pos, pipe.topPipeHeight])

        states = []
        for bird in self.birds:
            states.append(torch.Tensor([bird.y, bird.velocity] + pipeState))

        return states

    def draw(self, screen, mode):
        screen.blit(background, (0, 0))

        for pipe in self.pipes:
            pipe.draw(screen)
        for bird in self.birds:
            bird.draw(screen)

        if mode == "human":
            pointsStr = ' '.join([chr(i+65) + ":" + str(bird.points) for i, bird in enumerate(self.birds)])
            text = self.font.render(pointsStr, True, "white")
            screen.blit(text, (int(screenWidth/2 - text.get_size()[0]/2), textY))

        elif mode == "computer":
            points = 0
            for bird in self.birds:
                points = max(points, bird.points)
            text = self.font.render(str(points), True, "white")
            screen.blit(text, (int(screenWidth/2 - text.get_size()[0]/2), textY))

    def getPoints(self):
        return np.array([bird.points for bird in self.birds])

    def collision(self, bird):
        birdRect = bird.getRect()
        for pipe in self.pipes:
            for pipeRect in pipe.getRects():
                if birdRect.colliderect(pipeRect):
                    return True
        return False

    def birdInPipe(self, bird):
        birdRect = bird.getRect()
        for pipe in self.pipes:
            if birdRect.colliderect(pipe.getSpace()):
                return True
        return False

    def makePipes(self, numPipes):
        pipes = []
        for i in range(numPipes):
            pos = int(screenWidth+ i/numPipes * (screenWidth + Pipe.width))
            pipes.append(Pipe(pos))
        return pipes