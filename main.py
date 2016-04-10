import pygame, sys, Funk
from tileC import Tile
from object_classes import *
from interaction import interaction
from A_Star import A_Star

__author__ = 'Bhavik & Ram'

pygame.init() #initializing pygame
pygame.font.init() #displaying font in screen
pygame.mixer.init() #initializing mixed components of pygame

pygame.mixer.music.load('audio/zombie_theme.ogg')
pygame.mixer.music.play(-1) #-1 means the music will play infinite times until the game stop

screen = pygame.display.set_mode((704, 448)) # 32, 32  #creating display

"""
putting tiles to our screen
"""
for y in range(0, screen.get_height(), 32):
    for x in range(0, screen.get_width(), 32):
        if Tile.total_tiles in Tile.invalids:
            Tile(x, y, 'solid')
        else:
            Tile(x, y, 'empty')

"""
"""

clock = pygame.time.Clock()
FPS = 20
total_frames = 0
dungeon = pygame.image.load('images/dungeon.jpg')
survivor = Survivor(32 * 2, 32 * 4)


while True:

    screen.blit(dungeon, (0,0) ) #after making move, it will erase our last position

    Zombie.spawn(total_frames, FPS)
    Zombie.movement()

    survivor.movement()

    Bullet.super_massive_jumbo_loop(screen)

    A_Star(screen, survivor, total_frames, FPS) #calling A_Star
    interaction(screen, survivor)
    Tile.draw_tiles(screen) #drawing tiles
    survivor.draw(screen)
    Zombie.draw_zombies(screen)

    #print survivor.get_number()
    #print zombie1.get_number()

    pygame.display.flip()
    clock.tick(FPS)
    total_frames += 1
