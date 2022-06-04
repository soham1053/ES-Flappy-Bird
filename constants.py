import pygame

size_factor = 1

background = pygame.image.load('background.png')
background = pygame.transform.scale(background, [size*size_factor for size in background.get_size()])

screenWidth, screenHeight = background.get_size()

birdX = 40

ground = 282*size_factor
textY = 25*size_factor

jumpSpeed = -9
gravity = 1

pipeColor = (100, 255, 100)