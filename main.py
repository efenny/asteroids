import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

dt = 0
running = True

def main():
    success, failure = pygame.init()

    if success:
        clock = pygame.time.Clock()

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            screen.fill(pygame.Color(0,0,0))
            pygame.display.flip()

            dt = clock.tick(60) / 1000


    elif failure:
        raise Exception('failed to init pygame')
    else:
        raise Exception('unreachable')


if __name__ == "__main__":
    main()
