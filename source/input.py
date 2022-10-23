#!/usr/bin/env python3
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((100, 100))
r = True

def exit():
    global r
    r = False
    print('Rover control closed')


def main():
    global r
    while r:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_f:
                    print('L motor')
                if event.key == pygame.K_j:
                    print('R motor')

        pygame.display.update()


if __name__ == "__main__":
    print('Rover control is online')
    main()
