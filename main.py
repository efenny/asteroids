import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

dt = 0
running = True

def main():
    success, failure = pygame.init()

    if success:
        clock = pygame.time.Clock()

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        Player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            screen.fill(pygame.Color(0,0,0))
            Player1.draw(screen)

            pygame.display.flip()
            dt = clock.tick(60) / 1000

            Player1.update(dt)


    elif failure:
        raise Exception('failed to init pygame')
    else:
        raise Exception('unreachable')


if __name__ == "__main__":
    main()
