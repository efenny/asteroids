import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

dt = 0
running = True

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

def checkToExit():
    for event in pygame.event.get():
        return event.type == pygame.QUIT

def main():
    success, failure = pygame.init()

    if success:
        clock = pygame.time.Clock()

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        AsteroidField.containers = (updatable)
        Asteroid.containers = (asteroids, updatable, drawable)
        Player.containers = (updatable, drawable)
        Shot.containers = (updatable, drawable, shots)
        Player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        AsteroidField()

        while running:
            if checkToExit():
                return

            screen.fill(pygame.Color(0,0,0))

            for d in drawable:
                d.draw(screen)

            pygame.display.flip()
            dt = clock.tick(60) / 1000

            for u in updatable:
                u.update(dt)

            for a in asteroids:
                if a.hasCollided(Player1):
                    print("Game over!")
                    return

                for s in shots:
                    if a.hasCollided(s):
                        a.split()
                        s.kill()

    elif failure:
        raise Exception('failed to init pygame')
    else:
        raise Exception('unreachable')


if __name__ == "__main__":
    main()
