import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    success, failure = pygame.init()

    if success:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return


            screen.fill(pygame.Color(0,0,0))
            pygame.display.flip()


    elif failure:
        raise Exception('failed to init pygame')
    else:
        raise Exception('unreachable')


if __name__ == "__main__":
    main()
