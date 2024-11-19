import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time_clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(x = (SCREEN_WIDTH / 2), y = (SCREEN_HEIGHT / 2))

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = time_clock.tick(60) / 1000
        screen.fill((0,0,0))
        for x in drawable:
            x.draw(screen)
        for x in updatable:
            x.update(dt)
        pygame.display.flip()

if __name__ == "__main__":
    main()