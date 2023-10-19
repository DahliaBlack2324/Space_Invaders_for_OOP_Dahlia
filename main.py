import pygame
import sys
from gg import GG

def start_game():
    pygame.init()
    screen = pygame.display.set_mode((1600,900))
    pygame.display.set_caption("?????")

    flag = True
    gg = GG(screen)
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()
        gg.output()

start_game()
