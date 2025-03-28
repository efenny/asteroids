import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, 'containers'):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def hasCollided(self, circle):
        return self.position.distance_to(circle.position) < self.radius

    def draw(self, screen):
        # sub-classes must overwrite
        pass

    def update(self, dt):
        # sub-classes must overwrite
        pass
