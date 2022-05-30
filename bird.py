import pygame
from constants import *


class Bird:
    img = pygame.transform.scale(pygame.image.load("bird.png"), (50, 50))
    x = screenWidth // 4

    def __init__(self):
        self.y = int(screenHeight/2 - self.img.get_size()[1]/2)
        self.velocity = 0
        self.dead = False
        self.points = 0

    def move(self, jump):
        if jump and not self.dead:
            self.velocity = jumpSpeed

        self.y += self.velocity
        self.velocity += gravity

        if self.hitGround():
            self.y = ground - self.img.get_size()[1]

        if self.y < 0:
            self.y = 0

    def die(self):
        if not self.dead:
            self.dead = True
            self.velocity = 0

    def gainPoint(self):
        if not self.dead:
            self.points += 1

    def hitGround(self):
        return self.y + self.img.get_size()[1] >= ground

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def getRect(self):
        return pygame.rect.Rect((self.x, self.y), self.img.get_size())