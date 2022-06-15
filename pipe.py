from constants import *
import pygame
import random


class Pipe:
    width = 50
    speed = 10
    verticalSpace = 200

    def __init__(self, startX):
        self.pos = startX
        self.topPipeHeight = int(random.random() * (ground - self.verticalSpace))

    def move(self):
        self.pos -= self.speed
        if self.pos + self.width < 0:
            self.pos += screenWidth + self.width
            self.topPipeHeight = int(random.random() * (ground - self.verticalSpace))

    def stop(self):
        self.speed = 0

    def draw(self, screen):
        pygame.draw.rect(screen, pipeColor, (self.pos, 0, self.width, self.topPipeHeight))
        pygame.draw.rect(screen, pipeColor, (self.pos, self.topPipeHeight + self.verticalSpace, self.width, ground - (self.topPipeHeight + self.verticalSpace)))

    def getRects(self):
        return [pygame.rect.Rect(self.pos, 0, self.width, self.topPipeHeight),
                pygame.rect.Rect(self.pos, self.topPipeHeight + self.verticalSpace, self.width, ground - (self.topPipeHeight + self.verticalSpace))]

    def getSpace(self):
        return pygame.rect.Rect(self.pos, self.topPipeHeight, self.width, self.verticalSpace)