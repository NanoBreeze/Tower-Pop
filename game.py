import pygame
import pygame.locals
import sys
import pygame.sprite

import balloon
import tower
import sprite_groups
import colours
import path
import logging
import logging.config



logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('simpleLogger')





pygame.init()

DISPLAYSURF=pygame.display.set_mode((400,300))
pygame.display.set_caption('ML Tower Defence')

main_path = path.Path()

linear_tower = tower.create_tower(tower.LINEAR_TOWER, (150, 150), DISPLAYSURF)
three_sixty_tower = tower.create_tower(tower.THREE_SIXTY_TOWER, (80, 100), DISPLAYSURF)
teleportation_tower = tower.create_tower(tower.TELEPORTATION_TOWER, (150, 250), DISPLAYSURF)
explosion_tower = tower.create_tower(tower.EXPLOSION_TOWER, (150, 50), DISPLAYSURF)

b1= balloon.create_balloon_context(balloon.BALLOON_L5, main_path, 0)
assert type(b1) is balloon.BalloonContext, 'b1 is not a BalloonContext'

sprite_groups.tower_sprites.add(linear_tower, three_sixty_tower, teleportation_tower, explosion_tower)

sprite_groups.ballon_sprites.add(b1)



fpsClock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type==pygame.locals.QUIT:
            pygame.quit()
            sys.exit()

    #tower_sprites.update()
    DISPLAYSURF.fill(colours.BLACK)
    sprite_groups.tower_sprites.update(sprite_groups.ballon_sprites, sprite_groups.bullet_sprites)
    sprite_groups.tower_sprites.draw(DISPLAYSURF)

    sprite_groups.ballon_sprites.update(sprite_groups.bullet_sprites)
    sprite_groups.ballon_sprites.draw(DISPLAYSURF)

    sprite_groups.bullet_sprites.update()
    sprite_groups.bullet_sprites.draw(DISPLAYSURF)


    fpsClock.tick(15)
    pygame.display.update()


