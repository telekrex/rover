#!/usr/bin/env python3
# Input service - turns controller into COM data

import pygame
from pygame.locals import *
pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()
js = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]


def clamp():
    return ''


# while True:
#     for event in pygame.event.get():
#         if event.type == JOYAXISMOTION:
#             print(event)


if __name__ == "__main__":
    print('working')
