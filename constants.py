import pygame

background = pygame.image.load('background.png')

screenWidth, screenHeight = background.get_size()

ground = 282
textY = 25

jumpSpeed = -9
gravity = 1

pipeColor = (100, 255, 100)