#!/usr/bin/env python

import pygame
from gridmap import GridMap
from maps import TestMap

X = 0
Y = 1

TILE_SZ = (32, 32)
SCREEN_SZ = (640, 480)

if '__main__' == __name__:

   screen = pygame.display.set_mode( SCREEN_SZ )
   running = True
   clock = pygame.time.Clock()

   tilesheet = pygame.image.load( 'Game/mapd01a.png' )
   tilesheet_w = tilesheet.get_width() / TILE_SZ[X]
   gmap = GridMap( TestMap )

   vx = SCREEN_SZ[X] / 2
   #vy = SCREEN_SZ[Y] / 3
   vy = 0

   tilesheet.set_colorkey( (0, 0, 0) )

   while running:
      for event in pygame.event.get():
         if pygame.QUIT == event.type:
            running = False
         elif pygame.KEYDOWN == event.type:
            if pygame.K_ESCAPE == event.key:
               running = False

      keys = pygame.key.get_pressed()
      #if keys[pygame.K_RIGHT]:
      #if keys[pygame.K_LEFT]:
      #if keys[pygame.K_UP]:

      for layer in gmap.tiles:
         x = 0
         y = 0
         for row in layer:
            x = 0
            y += 1
            for tile_id in row:
               x += 1

               screen_x = int( (((x - y) * TILE_SZ[X] / 2) + vx ) )
               screen_y = int( ((x + y) * TILE_SZ[Y] / 3.55) + vy )

               tilerect = [
                  (tile_id % tilesheet_w) * TILE_SZ[X],
                  (tile_id / tilesheet_w) * TILE_SZ[Y],
                  TILE_SZ[X],
                  TILE_SZ[Y] ]

               screen.blit( tilesheet, (screen_x, screen_y), tilerect )

      pygame.display.flip()

      clock.tick( 60 )

