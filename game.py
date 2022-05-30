from bird import Bird
from pipe import Pipe
from constants import *
import pygame

class FlappyBird:
    def __init__(self, numPipes):
        self.pipes = self.makePipes(numPipes)
        self.bird = Bird()
        self.started = False
        self.font = pygame.font.SysFont("Impact", 90, False)

    def reset(self):
        self.bird = Bird()
        self.pipes = self.makePipes(len(self.pipes))
        self.started = False

    def step(self, jump):
        if jump:
            self.started = True

        if self.started:
            if self.collision() or self.bird.hitGround():
                self.bird.die()

            if self.birdInPipe() and not self.entered:
                self.entered = True
                self.bird.gainPoint()
            elif not self.birdInPipe():
                self.entered = False

            self.bird.move(jump)
            for pipe in self.pipes:
                pipe.move()

    def draw(self, screen):
        screen.blit(background, (0, 0))

        for pipe in self.pipes:
            pipe.draw(screen)
        self.bird.draw(screen)

        text = self.font.render(str(self.bird.points), True, "white")
        screen.blit(text, (int(screenWidth/2 - text.get_size()[0]/2), textY))

    def collision(self):
        birdRect = self.bird.getRect()
        for pipe in self.pipes:
            for pipeRect in pipe.getRects():
                if birdRect.colliderect(pipeRect):
                    return True
        return False

    def birdInPipe(self):
        birdRect = self.bird.getRect()
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