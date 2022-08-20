#!/usr/bin/env python3
# USBinput service - turns controller input into COM data

import pygame
pygame.init()
pygame.joystick.init()
js = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]



def clamp():
    return ''



while True:

    for event in pygame.event.get():
        if event.type == JOYAXISMOTION:
            print(event)






if __name__ == "__main__":
    print('working')
